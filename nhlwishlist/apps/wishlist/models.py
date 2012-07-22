from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class WishTag(models.Model):
    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=6)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return '/tags/%s/' % self.name
    
    
class Wish(models.Model):
    author = models.ForeignKey(User)
    subject = models.CharField(max_length=140)
    #subject_slug = models.SlugField(max_length=45)
    wish = models.TextField()
    tags = models.ManyToManyField(WishTag)
    votes = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=datetime.now())
    date_edited = models.DateTimeField(default=datetime.now())
    deleted = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.wish
    
    class Meta:
        ordering = ["-date_added"]
        verbose_name_plural = "wishes"
    
    @models.permalink    
    def get_absolute_url(self):
        return '/wishes/%s/' % self.id
