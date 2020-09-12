import database.colaborador.consulta 	as colaboradorQuery
import database.segurado.consulta 		as seguradoQuery
import database.segurado.criar			as seguradoCreate
import database.criar 					as criar
import database.control					as c
import app								as a
import os								as os
import requests
from pprint import pprint as pprint
from flask 	import render_template
from flask 	import session
from flask 	import redirect
from flask 	import request
from flask 	import Flask
from flask 	import url_for

control 		= c.Control()
principal 		= a.Principal(control)
app 			= principal.createApp()
app.secret_key 	= os.urandom(16)
consultaSegurado 		= seguradoQuery.ConsultaBanco(control)
consultaColaborador		= colaboradorQuery.ConsultaBanco(control)
criarSegurado			= seguradoCreate

class servidor:
	

	@app.route("/", methods=['GET'])
	def index():
		if (verificacaoDeSessao()):
			if (consultaSegurado.seguradoExiste()):
				return redirect('/logando')

			if (consultaColaborador.colaboradorExiste()):
				return redirect('/logando')
		else:
			return render_template('index.html')

	@app.route("/logando", methods=['POST', 'GET'])	
	def logando():
		if(request.method == 'POST'):
			form 	= request.form
			control.setEmail(form.get('email'))
			control.setSenha(form.get('senha'))

			if(consultaColaborador.colaboradorExiste()):
				session['email'] = control.getEmail()
				session['senha'] = control.getSenha()
				return redirect('/caixa_de_entrada')

			elif(consultaSegurado.seguradoExiste()):
				session['email'] = control.getEmail()
				session['senha'] = control.getSenha()
				return redirect('/home')
			else:
				return render_template('index.html', msg='Erro: Email ou Senha inválida')

		if (verificacaoDeSessao()):
			control.setEmail(session['email'])
			control.setSenha(session['senha'])

			if (consultaSegurado.seguradoExiste()):
				return redirect('/home')

			if (consultaColaborador.colaboradorExiste()):
				return redirect('/caixa_de_entrada')

		else:
			return redirect('/')

	@app.route('/caixa_de_entrada', methods=['GET'])
	def caixa_de_entrada():
		if (	verificacaoDeSessao() and
				consultaColaborador.colaboradorExiste()):
			control.setEmail(session['email'])
			control.setSenha(session['senha'])
			return render_template('caixa_de_entrada.html')
		return redirect('/')

	@app.route("/home",methods=['GET'])
	def home():
		if (	verificacaoDeSessao() and
				consultaSegurado.seguradoExiste()):
			control.setEmail(session['email'])
			control.setSenha(session['senha'])
			return render_template('home.html')
		return redirect('/')

	@app.route("/logout", methods=['POST','GET'])
	def logout():
		if verificacaoDeSessao:
			session.pop('email', None)
			session.pop('senha', None)
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
		servidor.pegar_endereco()
		return '<b align="center">SUCESSO!!!</b>'

	def pegar_endereco():
		response = requests.get(control.getLocalizacao())
		print('\n')
		pprint(response.json()['data'])
		print('\n SUCESSO!!!')

# ESQUECE QUE ISSO AQUI EXISTE!!! NÃO MEXA!!!
def verificacaoDeSessao():
	if (('email' in session)and
		('senha' in session)):
		control.setEmail(session['email'])
		control.setSenha(session['senha'])
		return True
	return False

def iniciar():
	app.url_map.strict_slashes = False
	criar.tabela()
	app.run(debug=True, host='127.0.0.1', port = 8080)

if __name__ == "__main__":
	iniciar()