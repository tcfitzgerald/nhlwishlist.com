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
        return self.subject
    
    class Meta:
        ordering = ["-date_added"]
        verbose_name_plural = "wishes"
    
    @models.permalink    
    def get_absolute_url(self):
        return '/wishes/%s/' % self.id
    
class WishVote(models.Model):
    wish = models.ForeignKey(Wish)
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(default=datetime.now())
    
    def __unicode__(self):
        return self.wish.subject
    
    def save(self, *args, **kwargs):
        self.wish.votes = self.wish.votes + 1
        self.wish.save()
        
        self.user.get_profile().vote_count -= 1
        self.user.get_profile().save()
        super(WishVote, self).save(*args, **kwargs)
