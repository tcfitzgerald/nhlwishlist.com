from django.db import models

class Subscriber(models.Model):
    subscriber_email_address = models.EmailField(blank=False, unique=True)
    
    def __unicode__(self):
        return self.subscriber_email_address
