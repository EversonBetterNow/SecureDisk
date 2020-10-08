import os
import requests
import codecs
import itens.builder as builder_itens
from pprint import pprint as pprint
from flask 	import render_template
from flask 	import render_template_string
from flask 	import session
from flask 	import redirect
from flask 	import request
from flask 	import Flask
from flask 	import url_for
#
#132anderson@gmail.com
#securedisk@2020
# 
#132anderson@portoseguro.com
#securedisk@2020
#
pesquisa_cordenadas_gps = 'http://api.positionstack.com/v1/reverse?access_key=dc2e79642768afb966b7e46b48ec1b0b&query='
app = Flask(__name__, template_folder='views/', static_folder="views/static/")
app.secret_key 	= os.urandom(16)
class servidor:

	@app.route("/testar_layout", methods=['GET'])
	def testar_layout():
		item = builder_itens.build()
		pets = item.listPet()
		f = codecs.open("caixa_de_entrada.html", 'r')
		f = f.read()
		f = f.replace(r'{itens}', pets[0])
		f = f.replace(r'{itens_totais}', pets[1])
		return render_template_string('caixa_de_entrada.html')


	#Login
	@app.route("/", methods=['GET'])
	def index():
		if (verificacaoDeSessao()!=None):
			return redirect('/logando')
		else:
			return render_template('index.html')

	#Requisição e validação
	@app.route("/logando", methods=['POST', 'GET'])	
	def logando():
		if(request.method == 'POST'):
			form = request.form
			if(verificaLogin(form.get('mail'), form.get('password'), form.get('optradio'))):
				if(form.get('optradio') == 'insured'):
					return redirect('/home')

				elif(form.get('optradio') == 'provider'):
					return redirect('/caixa_de_entrada')

				else:
					'congratulations! <br> erro_type: super'
			else:
				return render_template('index.html', msg='Erro: Email ou senha inválida')

		elif (verificacaoDeSessao()=='insured'):
			return redirect('/home')

		if (verificacaoDeSessao()=='provider'):
			return redirect('/caixa_de_entrada')

		else:
			return redirect('/')

	#Pagina principal COLABORADOR
	@app.route('/caixa_de_entrada', methods=['GET'])
	def caixa_de_entrada():
		if (verificacaoDeSessao()=='provider'):
			return render_template('caixa_de_entrada.html')
		return redirect('/')

	#Pagina principal SEGURADO
	@app.route("/home",methods=['GET'])
	def home():
		print(verificacaoDeSessao())
		if (verificacaoDeSessao()=='insured'):
			return render_template('home.html')
		return redirect('/')

	#Layout_pet
	@app.route("/pet", methods=['POST','GET'])
	def pet():
		if (verificacaoDeSessao()=='insured'):
			return render_template('pet.html')
		return redirect('/')

	#Sair
	@app.route("/logout", methods=['POST','GET'])
	def logout():
		if verificacaoDeSessao():
			session.pop('mail', None)
			session.pop('password', None)
			session.pop('type', None)
		return redirect('/')

	
	#Incrementar para layout de convênio(MAIS TARDE)
	@app.route("/saude_pessoal", methods=['POST','GET'])
	def saude():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
	
	#Incrementar para layout de mecanica(MAIS TARDE)
	@app.route("/mecanica", methods=['POST','GET'])
	def mecanica():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
	#Incrementar para layout de advocacia(MAIS TARDE)
	@app.route("/advocacia", methods=['POST','GET'])
	def advocacia():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
	#Seria usado para criar um layout de discagem(provávelmente será excluído)
	@app.route("/emergencia", methods=['POST','GET'])
	def emergencia():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
	#Incrementar para entra na caixa de emergencias
	@app.route("/caixa_de_emergencias", methods=['POST','GET'])
	def caixa_de_emergencias():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
	#Incrementar para entra na caixa de agendamento
	@app.route("/caixa_de_agendamentos", methods=['POST','GET'])
	def caixa_de_agendamentos():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''

	#Url usado pelo app
	@app.route("/emergencia/geolocation/<string:latitude>,<string:longitude>", methods=['GET'])
	def teste(latitude, longitude):
		location = pesquisa_cordenadas_gps + latitude + ',' + longitude
		response = requests.get(location)
		print('\n')
		pprint(response.json()['data'])
		print('\n SUCESSO!!!')
		return '<b align="center">SUCESSO!!!</b>'

############################################################################
# ESQUECE QUE ISSO AQUI EXISTE!!! NÃO MEXA!!!
# Verifica se existe alguma variável de sessão
def verificacaoDeSessao():
	if (('mail' in session)and
		('password' in session)and
		('type') in session):
		return session['type']
	return None

# UPGRADE #
def verificaLogin(email, password, typee):
	#formato json para falha {'message': 'Invalid credentials'}
	#montando requisição json
	loginData 	= {"email":email, "password":password}
	response 	= requests.post('http://127.0.0.2:8080/api/login', json=loginData)
	jason 		= response.json()
	# print()
	# pprint(jason)
	# print()
	if('message' in jason.keys()):
		return False
	else:
		if(typee != jason['type_user']):
			return False
	#criando sessão para mante login
	session['type']		= typee
	session['mail'] 	= email
	session['password'] = password
	print(session['type'])
	return True

########################################################
config={
		'DEBUG':'True',
		'CACHE_TYPE': 'simple',
		'CACHE_REDIS_HOST': '127.0.0.1',
		'CACHE_REDIS_PORT': '8000',
		'CACHE_REDIS_URL': 'simple://127.0.0.1:8000'
	}

if __name__ == "__main__":
	print('Initilizing application')
	app.config.from_mapping(config)
	app.config.from_object(config)
	app.run(debug=True, host='127.0.0.1', port = 8000)

# Exemplo de retorno (apagarás em breve)
#{
#    "first_name":"Anderson",
#    "last_name":"kan",
# 		"cpf":"460.661.888-66",
#    "tel":"(11)4616-4117",
#    "cel":"(11)97553-9825",
#    "email":"132anderson@gmail.com",
# 	 "password":"securedisk@2020",
# 	"type_user":"insured"
# }