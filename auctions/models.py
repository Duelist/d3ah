from d3ah.settings import DBNAME
from mongoengine import *

connect(DBNAME)

AUCTION_TYPES = (
    ('sc','Softcore'),
    ('hc','Hardcore'),
)

AUCTION_RULES = (
    ('dur','Duration'),
    ('mnp','Minimum Price'),
)

AUCTION_STATES = (
	('hd', 'Hidden'),
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

class Affix(EmbeddedDocument):
    type = StringField(max_length=3, choices=AFFIX_TYPES, required=True)
    value = IntField(required=True)

class Item(EmbeddedDocument):
    name = StringField(max_length=120, required=True)
    type = StringField(max_length=2, choices=ITEM_TYPES, required=True)
    level = IntField(min_value=1, max_value=80, required=True)
    item_level = IntField(min_value=1, max_value=83, required=True)
    affixes = ListField(EmbeddedDocumentField(Affix))

class Rule(EmbeddedDocument):
    type = StringField(max_length=3, choices=AUCTION_RULES, required=True)
    value = IntField(required=True)

class Bid(EmbeddedDocument):
    bidder_id = IntField(min_value=1, required=True)
    value = FloatField(min_value=0, required=True)

class Auction(Document):
    user_id = IntField(min_value=1, required=True)
    type = StringField(max_length=2, choices=AUCTION_TYPES, required=True)
    state = StringField(max_length=2, choices=AUCTION_STATES, required=True)
    created_date = DateTimeField(required=True)
    item = EmbeddedDocumentField(Item)
    rules = ListField(EmbeddedDocumentField(Rule))