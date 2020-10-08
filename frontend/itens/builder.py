import itens.elements as e
import requests
# from pprint import pprint as pprint

class build:

	def listPet(self):
		total = 1
		self.listas = ""
		item 		= e.elemento()
		response 	= requests.get('http://127.0.0.2:8080/api/pet')
		jason 		= response.json()

		for i in jason:
			total += 1
			self.listas += item.lista(i['id'], i['name'])

		for count in range(2,10):
			total += 1
			self.listas += item.lista(count,'testando'+str(count))

		return [self.listas, total]