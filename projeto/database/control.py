class Control:
	def __init__(self):
		self.key 		= 'dc2e79642768afb966b7e46b48ec1b0b'
		self.url		= 'http://api.positionstack.com/v1/reverse?access_key='+ self.key +'&query='
		self.email 		= ''
		self.senha 		= ''
		self.latitude 	= ''
		self.longitude 	= ''

	def getEmail(self):
		return self.email

	def getSenha(self):
		return self.senha

	def getUrl(self):
		return self.url

	def getLatitude(self):
		return self.latitude

	def getLongitude(self):
		return self.longitude

	def getLocalizacao():
		return control.getUrl()+control.getLatitude()+','+control.getLongitude()

	def setEmail(self, email):
		self.email = email

	def setSenha(self, senha):
		self.senha = senha

	def setLatitude(self, latitude):
		self.latitude = latitude

	def setLongitude(self, longitude):
		self.longitude = longitude
		
	