from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from models import initialize_database
from os import environ
from resources import initialize_resources
from schema.schema import Schema


application = Flask(__name__)

# load de variáveis de ambiente
print('Loading environment variables from .env file')
load_dotenv('./environments/local.env')

# load das variaveis de ambiente dentro do flask
for item in environ.items():
    application.config[item[0]] = item[1]

# definição de CORS
if not environ.get('CORS_URL', None):
    CORS(application, supports_credentials=True, origins="*")
else:
    print(environ.get('CORS_URL'))
    CORS(application, resources={r"*": {"origins": environ.get('CORS_URL')}})

# start no database
initialize_database(application)

# Starting RESTful endpoints
initialize_resources(application)


@application.before_request
def startup():
    print("Initializing migration DB")
    Schema.migration()

config={
		'DEBUG':'True',
		'CACHE_TYPE': 'simple',
		'CACHE_REDIS_HOST': '127.0.0.2',
		'CACHE_REDIS_PORT': '8080',
		'CACHE_REDIS_URL': 'simple://127.0.0.2:8080'
	}
# Run application
if __name__ == '__main__':
    print('Initilizing application')
    application.config.from_mapping(config)
    application.config.from_object(config)
    application.run(debug=True, host='127.0.0.2', port = 8080)
