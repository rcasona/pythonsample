from google.appengine.ext import ndb
import time

class User(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	updated = ndb.DateTimeProperty(auto_now_add=True)
	fname = ndb.StringProperty()
	lname = ndb.StringProperty()
	dname = ndb.StringProperty()
	email = ndb.StringProperty()
	password = ndb.StringProperty()


