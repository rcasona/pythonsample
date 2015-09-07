import webapp2
import datetime
import jinja2
import logging
import json as simplejson
import time
from session import session

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('frontend'), autoescape=True)

class BaseHandler(webapp2.RequestHandler):
	def __init__(self, request = None, response = None):
		self.initialize(request, response)
		self.now = datetime.datetime.now()
		self.tv = {}
		self.message = None
		self.error = None
		self.session = session.get_session()
		self.user = session.get_current_user(self.session)

	def render(self, template_path=None, force=False):
		self.tv["user"] = self.user
		self.tv["current_timestamp"] = time.mktime(self.now.timetuple())
		self.tv["error"] = self.request.get("error")
		self.tv["message"] = self.message


		template = jinja_environment.get_template(template_path)
		self.response.out.write(template.render(self.tv))

	def logged_this_user(self, user):
		session.login(user)

	def logout(self):
		if self.session.is_active():
			self.session.terminate()

