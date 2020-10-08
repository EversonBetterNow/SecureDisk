class elemento:
	def __init__(self):
		print("\n\nsucesso!\n\n")
		self.text = ""
		self.key = ""

	def lista(self, key, text):
		self.text 	= text
		self.key	= key
		return '''
		<li class="list-group-item" >
			<div class="pull-right action-buttons">
				<a href="http://www.jquery2dotnet.com"><span class="glyphicon glyphicon-pencil"></span></a>
				<a href="http://www.jquery2dotnet.com" class="trash"><span class="glyphicon glyphicon-trash"></span></a>
				<br>
			</div>
			<div class="checkbox">
			<input type="checkbox" id='''+str(self.key)+''' />
			<label for='''+str(self.key)+'''>
			'''+self.text+'''
			</label>
			</div>
		</li>
'''