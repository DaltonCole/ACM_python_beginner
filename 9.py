from dummy import Dummy
from random import randint

class Smart < dummy:
	def __init__(self, name):
		Smart.dum_people -= 1
		Smart.smart_people += 1

		self.name = name
		self.value = randint(0,9)

	def update_smart_people(self, people):
		smart_people = people