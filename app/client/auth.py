from evernote.api.client import EvernoteClient

class Auth(object):
	"""Authenticates a user to evernote based on the developer token, oauth access token"""

	#Developer Access token
	#OAuth Client and Consumer key can also be used for the same
	ACCESS_TOKEN = ""

	def get_access_token(self):
		"""Returns the access token specified by our application"""
		return self.ACCESS_TOKEN;

	def authenticate(self):
		"""Authenticates the user using evernotes api"""
		return EvernoteClient(token=self.get_access_token(), sandbox=True)