from django import template
from django.utils.timesince import timesince
from datetime import datetime
from postmarkup import render_bbcode
from django.utils.safestring import mark_safe
from django.contrib.comments.models import Comment

register = template.Library()

@register.filter
def timeago(value, arg=None):
    """Formats a date as the time since that date ("2 hours ago")."""
    
    if not value:
        return u''
    try:
        if arg:
            return timesince(value, arg)
        timeagoval = timesince(value).split(",")[0]
        if timeagoval == "0 minutes":
            return "just now"
        else:
            return "%s ago" % timeagoval
    except (ValueError, TypeError):
        return u''
timeago.is_safe = False

@register.filter
def bbcode(value):
    """BBcode template filter
    
    Runs the passed text through the bbcode parser
        
    """
    
    try:
        return mark_safe(render_bbcode(value))
    except:
        return value
bbcode.is_safe = True

@register.inclusion_tag('comments/recent_comments.html')
def recent_comments(request):
    comments = Comment.objects.filter(is_public=True,is_removed=False).order_by('-submit_date')[:5]
    return {'comments': comments}
