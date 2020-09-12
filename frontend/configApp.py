from flask import Flask

config={
		'DEBUG':'True',
		'CACHE_TYPE': 'simple',
		'CACHE_REDIS_HOST': '127.0.0.1',
		'CACHE_REDIS_PORT': '8000',
		'CACHE_REDIS_URL': 'simple://127.0.0.1:8000'
		}

def createApp():
	app = Flask(__name__, template_folder='views/')
	app.config.from_mapping(config)
	app.config.from_object(config)
	return app