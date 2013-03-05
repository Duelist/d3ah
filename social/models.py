from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    bnet_id = models.CharField('Battle.net ID', max_length=32)
    
    def __unicode__(self):
      return self.user.username;