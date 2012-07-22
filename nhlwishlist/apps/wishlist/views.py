from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from nhlwishlist.apps.wishlist.models import Wish, WishTag

from nhlwishlist.apps.wishlist.forms import WishForm

def index(request):
    
    q = request.GET.get('q', None)
    
    wishes = Wish.objects.filter(deleted=False)
    
    if q:
        if q == 'top':
            wishes = wishes.order_by("-votes")
    
    return render(request, 'base.html', {'wishes': wishes, 'q': q})
    
    
def summary(request, wish_id):
    wish = Wish.objects.get(pk=wish_id)
    
    return render(request, 'wishlist/wish.html', {'wish': wish})
    
    
def tags(request, name):
    
    tag = get_object_or_404(WishTag, name=name)
    
    wishes = Wish.objects.filter(tags=tag)
    
    return render(request, 'base.html', {'wishes': wishes})

@login_required    
def submit_wish(request):
    
    if request.method == "POST":
        form = WishForm(request.POST)
        if form.is_valid():
            
            tags = request.POST.getlist('tags')
            
            
            wish = Wish(author=request.user, subject=form.cleaned_data['subject'], wish=form.cleaned_data['wish'], date_added=datetime.now())
            wish.save()
            
            if tags:
                for id in tags:
                    tag = get_object_or_404(WishTag, pk=id)
                    
                    wish.tags.add(tag)
            
            return redirect('home')
            
    else:
        form = WishForm()
        
    return render(request, 'wishlist/submit_wish.html', {'form': form})
        