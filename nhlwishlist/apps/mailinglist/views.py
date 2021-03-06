from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from nhlwishlist.apps.mailinglist.models import Subscriber

def index(request):
    return render_to_response('mailinglist/index.html', context_instance=RequestContext(request))
    
def subscribe(request):
    
    if request.method == "POST":
        
        subscriber_email = request.POST['email']
        
        duplicate = Subscriber.objects.filter(subscriber_email_address=subscriber_email)
        
        if duplicate:
            return render_to_response('mailinglist/index.html', {'error_message': "You have already signed up!"}, context_instance=RequestContext(request))
        
        if subscriber_email:
            
            subscriber = Subscriber(subscriber_email_address=subscriber_email, date_subscribed=datetime.utcnow())
            subscriber.save()
            
            return render_to_response('mailinglist/index.html', {'success_message': "Thanks! We promise not to spam you and will let you know when we launch!"}, context_instance=RequestContext(request))
            
        else:
            return render_to_response('mailinglist/index.html', {'error_message': "You didn't enter an e-mail address!"}, context_instance=RequestContext(request))
            
            
    HttpResponseRedirect(reverse('home'))
