from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse
from nhlwishlist.apps.wishlist.models import Wish

def index(request):
    """ Default index view  """
    
    q = request.GET.get('q', None)
    
    wishes = Wish.objects.filter(deleted=False)
    
    if q:
        if q == 'top':
            wishes = wishes.order_by("-votes")
    
    return render(request, 'base.html', {'wishes': wishes, 'q': q})
