from hashlib import sha256
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    
    user = models.ForeignKey(User, unique=True, related_name="profile")
    location = models.CharField(max_length=125, blank=True)
    vote_count = models.IntegerField(default=10)
    invitation_code = models.CharField(max_length=125, blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    def can_vote(self):
        return self.vote_count > 0
    
    def add_votes(self, votes):
        self.vote_count += votes
        return self.save()

    def generate_invite(self):
        secret = settings.INVITE_SECRET
        invite = sha256(self.user.date_joined + self.user.username + secret).hexdigest()
        self.invitation_code = invite
        self.save()
