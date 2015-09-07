from models.user import User

def get_session():
	from gaesessions import get_current_session
	return get_current_session()

def get_current_user(session_user):
	if session_user.has_key("user"):
		user = User.get_by_id(session_user["user"])
		if user:
			return user
		else:
			return {}
	else:
		return None

def login(user):
	this_session = get_session()
	this_session["user"] = user.key.id()
	return