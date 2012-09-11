from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

AUCTION_TYPES = (('sc','Softcore'),('hc','Hardcore'))
AUCTION_RULES = (('dur','Duration'),('mnp','Minimum Price'))
AUCTION_STATES = (
	('av', 'Available'),
    ('pd','Pending'),
    ('cp', 'Complete'),
)

AFFIX_TYPES = (
    ('ias','Attack Speed %'),
    ('loh','Life on Hit'),
    ('hs','Has Sockets'),
    ('str','Strength'),
)

ITEM_TYPES = (
    ('wp', 'Weapon'),
    ('hm', 'Helm'),
    ('ch','Chest'),
)

class Item(models.Model):
    user = models.ForeignKey(User)
    type = models.CharField('Item Type', max_length=2, choices=ITEM_TYPES)
    name = models.CharField('Item Name', max_length=64)
    level = models.IntegerField('Required Level')
    item_level = models.IntegerField('Item Level')
    
    def __unicode__(self):
        return self.name
    
class Affix(models.Model):
    item = models.ForeignKey(Item)
    type = models.CharField('Affix Type', max_length=3, choices=AFFIX_TYPES)
    value = models.IntegerField('Affix Value')
    
    def __unicode__(self):
        return '(' + self.item.name + ') '  + dict(AFFIX_TYPES)[self.type] + ': ' + str(self.value)

class Auction(models.Model):
    item = models.OneToOneField(Item)
    type = models.CharField('Auction Type', max_length=2, choices=AUCTION_TYPES)
    state = models.CharField('Auction State', max_length=2, choices=AUCTION_STATES)
    created_date = models.DateTimeField('Date Created')
    
    def __unicode__(self):
        return self.item.name

class Rule(models.Model):
    auction = models.ForeignKey(Auction)
    type = models.CharField('Rule Type', max_length=3, choices=AUCTION_RULES)
    value = models.IntegerField('Rule Value')

class Bid(models.Model):
    user = models.ForeignKey(User)
    value = models.IntegerField('Bid Value')