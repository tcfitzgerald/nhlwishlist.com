from django import template
from django.utils.timesince import timesince
from datetime import datetime
from postmarkup import render_bbcode
from django.utils.safestring import mark_safe

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

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)
