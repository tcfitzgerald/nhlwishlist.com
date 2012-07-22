from django import forms
from django.forms import *
from markitup.widgets import MarkItUpWidget
from nhlwishlist.apps.wishlist.models import WishTag

class WishForm(Form):
    subject = CharField(max_length=140, required=True, label=u'Title')
    wish = CharField(required=True, label=u'Wish', widget=MarkItUpWidget)
    tags = ModelMultipleChoiceField(queryset=WishTag.objects.all())