from flask import Flask
import server as server

config={
		'DEBUG':'True',
		'CACHE_TYPE': 'simple',
		'CACHE_REDIS_HOST': '192.168.15.5',
		'CACHE_REDIS_PORT': '8080',
		'CACHE_REDIS_URL': 'simple://192.168.15.15:8080'
		}
class Principal():

	def __init__(self, control):
		self.control = control

	def createApp(self):
		app = Flask(__name__, template_folder='html/')
		app.config.from_mapping(config)
		app.config.from_object(config)
		return app

if __name__ == "__main__":
	server.iniciar()
