from d3ah.settings import DBNAME
from mongoengine.django.auth import User
from mongoengine import *

connect(DBNAME)

class AppUser(User):
    meta = {
        'allow_inheritance': True,
        'indexes': [
            {'fields': ['username'], 'unique': True},
            {'fields': ['email'], 'unique': True}
        ]
    }

    def __unicode__(self):
      return self.username;