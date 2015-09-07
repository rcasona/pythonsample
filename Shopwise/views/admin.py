import base
import logging
import datetime

from models.user import User
from models.products import Product


class IndexHandler(base.BaseHandler):
	def get(self):
		if not self.user:
			self.tv["product"] = Product.query().fetch()
			#logging.critical(self.tv["product"])
			self.render('dashboard.html')

		if self.user:
			self.tv["user"] = True
			self.tv["edit"] = True

			self.tv["product"] = Product.query(Product.owner == self.user.key).fetch()
			#logging.critical(self.tv["product"])
			self.render('dashboard.html')
		
class RegisterPage(base.BaseHandler):
	def get(self):
		self.render('registration.html')

	def post(self):
		fname = self.request.get("first_name")
		lname = self.request.get("last_name")
		dname = self.request.get("display_name")
		email = self.request.get("email")
		password = self.request.get("password")
		rpassword = self.request.get("password_confirmation")

		#logging.critical(email)

		if password != rpassword:
			self.error = "Password Not Match"
			self.redirect('/create/account?error='+self.error)

		user = User.get_by_id(id=email)
		logging.critical(user)

		if user:
			self.error = "Email already exists!"
			self.redirect('/create/account?error='+self.error)

		user = User(id=email)
		user.fname = fname
		user.lname = lname
		user.dname = dname
		user.email = email
		user.password = password
		user.put()
		self.logged_this_user(user)
		self.tv["user"] = True
		self.redirect('/dashboard')

class DashboardPage(base.BaseHandler):
	def get(self):
		self.tv["user"] = True
		self.tv["edit"] = False
		self.tv["product"] = Product.query().fetch()
		logging.critical(self.tv["product"])
		self.render('dashboard.html')
		
		

class LoginHandler(base.BaseHandler):
	def get(self):
		self.render("login.html")

	def post(self):
		email = self.request.get("email")
		password = self.request.get("password")
		user = User.get_by_id(id=email)
		if not user:
			self.error = "Email and Password not recognize"
			logging.critical(self.error)
			self.redirect('/?error='+self.error)
			return

		if user.password != password:
			self.error = "Email and Password not recognize"
			logging.critical(self.error)
			self.redirect("/?error="+self.error)
			return
		self.logged_this_user(user)
		self.redirect("/")

class LogoutHandler(base.BaseHandler):
    def get(self):
        self.logout()
        self.redirect("/")

class CreateProdPage(base.BaseHandler):
	def get(self):
		if self.user:
			self.render('createprod.html')

	def post(self):
		prodname = self.request.get("prod_name")
		description = self.request.get("description")
		price = self.request.get("price")
		qty = self.request.get("quantity")
		prod = Product()

		try:
			prod.prod_name = prodname
			prod.description = description
			prod.price =float(price)
			prod.quantity = int(qty)
			prod.owner = self.user.key
			prod.owner_name = self.user.email
			prod.put()
			self.message = "Successfully save"
			self.redirect('/create/prod')
		except:
			self.error = "Check Input"
			self.redirect('/create/prod?error='+self.error)
			return
class EditHandler(base.BaseHandler):
	def get(self,instance):
		self.tv["prod"]=Product.get_by_id(long(instance))
		instance = Product.get_by_id(long(instance))
		self.tv["instance"]=instance
		self.render("updateprod.html")

	def post(self,instance):
		instance = Product.get_by_id(long(instance))
		prodname = self.request.get("prod_name")
		description = self.request.get("description")
		price = self.request.get("price")
		qty = self.request.get("quantity")

		instance.prod_name = prodname
		instance.description = description
		instance.price = float(price)
		instance.quantity=int(qty)
		instance.put()
		self.redirect('/')


class DeleteHandler(base.BaseHandler):
	def get(self,instance):
		items = Product.get_by_id(long(instance))
		items.key.delete()
		self.redirect('/')

	
		








		






