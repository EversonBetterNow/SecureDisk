import sqlite3

def tabela():
	
	conn = sqlite3.connect('securedisk.db')
	c = conn.cursor()

	# Create table
	c.execute('''
		
		''')

	#c.execute("INSERT INTO segurado VALUES ('123','fulano','fulano@gmail.com','123')")

	conn.commit()
	conn.close()