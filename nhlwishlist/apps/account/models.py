from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, unique=True)
    location = models.CharField(max_length=125, blank=True)
    vote_count = models.IntegerField(default=10)
    
    def can_vote(self):
        return self.vote_count > 0
