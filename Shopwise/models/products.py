from google.appengine.ext import ndb
import time

class Product(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	update = ndb.DateTimeProperty(auto_now_add=True)
	description = ndb.StringProperty()
	prod_name = ndb.StringProperty()
	owner = ndb.KeyProperty()
	owner_name = ndb.StringProperty()
	price = ndb.FloatProperty()
	image = ndb.StringProperty()
	quantity = ndb.IntegerProperty()
