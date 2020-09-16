import controller.control					as c
import configApp					as a
import os
import requests
from pprint import pprint as pprint
from flask 	import render_template
from flask 	import session
from flask 	import redirect
from flask 	import request
from flask 	import Flask
from flask 	import url_for
#132anderson@gmail.com
#securedisk@2020

control 		= c.Control()
app 			= a.createApp()
app.secret_key 	= os.urandom(16)


class servidor:
	

	@app.route("/", methods=['GET'])
	def index():
		if (verificacaoDeSessao()):
			
			if (consultaSegurado.seguradoExiste()):
				return redirect('/logando')

			# if (consultaColaborador.colaboradorExiste()):
			# 	return redirect('/logando')
		else:
			return render_template('index.html')


	@app.route("/logando", methods=['POST', 'GET'])	
	def logando():
		if(request.method == 'POST'):
			form 	= request.form

			# if(consultaColaborador.colaboradorExiste()):
			# 	return redirect('/caixa_de_entrada')

			if(verificaLogin(form.get('mail'), form.get('password'))):
				return redirect('/home')
			else:
				return render_template('index.html', msg='Erro: Email ou senha inválida')

		elif (verificacaoDeSessao()):
			# if (consultaSegurado.seguradoExiste()):
			return redirect('/home')
			# if (consultaColaborador.colaboradorExiste()):
			# 	return redirect('/caixa_de_entrada')
		else:
			return redirect('/')


	@app.route('/caixa_de_entrada', methods=['GET'])
	def caixa_de_entrada():
		# if (	verificacaoDeSessao() and
		# 		consultaColaborador.colaboradorExiste()):
		# 	return render_template('caixa_de_entrada.html')
		return redirect('/')


	@app.route("/home",methods=['GET'])
	def home():
		if (verificacaoDeSessao()):
			return render_template('home.html')
		return redirect('/')



	@app.route("/logout", methods=['POST','GET'])
	def logout():
		if verificacaoDeSessao:
			session.pop('email', None)
			session.pop('password', None)
		return redirect('/')


	@app.route("/saude_pessoal", methods=['POST','GET'])
	def saude():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
	@app.route("/pet", methods=['POST','GET'])
	def pet():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''

	@app.route("/mecanica", methods=['POST','GET'])
	def mecanica():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''

	@app.route("/advocacia", methods=['POST','GET'])
	def advocacia():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''

	@app.route("/emergencia", methods=['POST','GET'])
	def emergencia():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''

	@app.route("/caixa_de_emergencias", methods=['POST','GET'])
	def caixa_de_emergencias():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''
			
	@app.route("/caixa_de_agendamentos", methods=['POST','GET'])
	def caixa_de_agendamentos():
		return '''
		<a type="button" class="home" href="/home"> 
			Helloworld
		</a>
			'''


	@app.route("/emergencia/geolocation/<string:latitude>,<string:longitude>", methods=['GET'])
	def teste(latitude, longitude):
		control.setLatitude(latitude)
		control.setLongitude(longitude)
		response = requests.get(control.getLocalizacao())
		print('\n')
		pprint(response.json()['data'])
		print('\n SUCESSO!!!')
		return '<b align="center">SUCESSO!!!</b>'


# ESQUECE QUE ISSO AQUI EXISTE!!! NÃO MEXA!!!
# Verifica se existe alguma variável de sessão
def verificacaoDeSessao():
	if (('email' in session)and
		('password' in session)):
		return True
	return False

# UPGRADE #
def verificaLogin(email, password):
	#formato json para falha {'message': 'Invalid credentials'}
	#montando requisição json
	loginData 	= {"email":email, "password":password}
	# pprint(loginData)
	# print()
	response 	= requests.post('http://127.0.0.1:8080/api/login', json=loginData)
	jason 		= response.json()
	# pprint(jason)
	# print()
	#Validação json
	if('message' in jason.keys()):
		return False
	else:
		#criando sessão para mante login
		session['email'] 	= email
		session['password'] = password
		return True

########################################################

def iniciar():
	app.url_map.strict_slashes = False
	app.run(debug=True, host='127.0.0.1', port = 8000)

if __name__ == "__main__":
	iniciar()
