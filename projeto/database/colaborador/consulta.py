import sqlite3
import database.control as c
from flask import g

DATABASE = 'securedisk.db'

class  ConsultaBanco:
	def __init__(self,control):
		self.control = control

	def colaboradorExiste(self):
		conn 	= sqlite3.connect(DATABASE)
		cursor 	= conn.cursor()
		
		# lendo os dados
		cursor.execute("""
		SELECT * FROM colaborador where email= ? and senha = ?;
		""", (
			self.control.getEmail(), 
			self.control.getSenha()
			)
		)

		bd = cursor.fetchall()
		conn.close()
		if len(bd) > 0:
			return True
		else:
			return False
