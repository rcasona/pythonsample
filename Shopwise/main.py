import webapp2

from views import admin as view
from webapp2_extras import routes
app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=view.IndexHandler, name="www-index"),
        webapp2.Route('/create/account', handler=view.RegisterPage, name="www-register"),
        webapp2.Route('/dashboard', handler=view.DashboardPage, name="www-dashboard"),
        webapp2.Route('/logout', handler=view.LogoutHandler, name="www-logout"),
        webapp2.Route('/login', handler=view.LoginHandler, name="www-login"),
        webapp2.Route('/create/prod', handler=view.CreateProdPage, name="www-create-prod"),
        webapp2.Route(r'/edit/<:.*>', handler=view.EditHandler, name="www-edit-handler"),
        webapp2.Route(r'/delete/<:.*>', handler=view.DeleteHandler, name="www-delete-handler"),


        #webapp2.Route('/login', handler=view.LoginHandler, name="www-login"),
        #webapp2.Route('/works', handler=view.WorkHandler, name="www-works"),
        #webapp2.Route('/logout', handler=view.LogoutHandler, name="www-logout"),
        #webapp2.Route(r'/info/<:.*>', handler=view.ClientInfoHandler, name="www-client-info-handler"),
        #webapp2.Route(r'/truckclient/<:.*>', handler=view.ClientTruck, name="www-truckclient"),
        #webapp2.Route(r'/rettruck/<:.*>', handler=view.RetrieveInfo, name="www-retrieve"),
        #webapp2.Route(r'/updateclient/<:.*>', handler=view.UpdateClient, name="www-update-client"),

        
    ])
])