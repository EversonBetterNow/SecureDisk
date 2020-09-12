class Control:
	def __init__(self):
		#Chave GPS
		self.key 		= 'dc2e79642768afb966b7e46b48ec1b0b'
		# Link GPS
		self.url		= 'http://api.positionstack.com/v1/reverse?access_key='+ self.key +'&query='
		# Coordenadas GPS
		self.latitude 	= ''
		self.longitude 	= ''
	def getUrl(self):
		return self.url

	def getLatitude(self):
		return self.latitude

	def getLongitude(self):
		return self.longitude

	def getLocalizacao():
		return control.getUrl()+control.getLatitude()+','+control.getLongitude()

	def setLatitude(self, latitude):
		self.latitude = latitude

	def setLongitude(self, longitude):
		self.longitude = longitude
		
	
