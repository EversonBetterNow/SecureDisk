import sqlite3

def tabela():
	conn = sqlite3.connect('securedisk.db')
	c = conn.cursor()

	# Create table
	c.execute('''
		CREATE TABLE IF NOT EXISTS segurado(
		proposta integer		not null CONSTRAINT proposta_segurado PRIMARY key, 
		nome 	varchar(100)	not null, 
		email 	varchar(100) 	not null, 
		senha 	varchar(20) 	not null);
		''')

	#c.execute("INSERT INTO segurado VALUES ('123','fulano','fulano@gmail.com','123')")

	conn.commit()
	conn.close()