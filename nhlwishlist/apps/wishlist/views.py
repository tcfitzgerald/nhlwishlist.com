from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages

from nhlwishlist.apps.wishlist.models import Wish, WishTag, WishVote

from nhlwishlist.apps.wishlist.forms import WishForm

def index(request):
    """ Old default index view """
    
    q = request.GET.get('q', None)
    
    wishes = Wish.objects.filter(deleted=False)
    
    if q:
        if q == 'top':
            wishes = wishes.order_by("-votes")
    
    return render(request, 'base.html', {'wishes': wishes, 'q': q})
    
    
def summary(request, wish_id):
    """ Show a wish
    
    The default view for showing an individual wish item
    
    """
    
    wish = Wish.objects.get(pk=wish_id)
    
    return render(request, 'wishlist/wish.html', {'wish': wish})
    
    
def tags(request, name):
    """ Show wishes by related tags """
    
    tag = get_object_or_404(WishTag, name=name)
    
    wishes = Wish.objects.filter(tags=tag)
    
    return render(request, 'base.html', {'wishes': wishes})

@login_required    
def submit_wish(request):
    """ Submit a wish
    
    Submit a wish to the site.  @login_required decorator forces login before
    a user can visit this view.
    
    """
    
    
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
    
@login_required
def vote(request, wish_id):
    """ Vote for a wish
    
    Increases the vote count for a wish.
    
    """
    
    wish = get_object_or_404(Wish, pk=wish_id)
    
    if request.user.get_profile().can_vote():
    
        vote = WishVote(user=request.user,wish=wish,date_added=datetime.now())
        vote.save()
        
        messages.add_message(request, messages.SUCCESS, 'Your vote has been recorded!')
        
    else:
        
        messages.add_message(request, messages.ERROR, 'You have run out of votes!')
        
    return redirect('wish_summary', wish.id)
        