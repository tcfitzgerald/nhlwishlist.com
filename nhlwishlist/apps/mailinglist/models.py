from django.db import models

class Subscriber(models.Model):
    subscriber_email_address = models.EmailField(blank=False, unique=True)
    date_subscribed = models.DateTimeField()
    
    def __unicode__(self):
        return self.subscriber_email_address
