from random import randint

class Dummy:
	dum_people = 0
	smart_people = 10

	def __init__(self, name):
		Dummy.dum_people += 1
		Dummy.smart_people -= 1

		self.name = name
		self.value = randint(0,9)

	def print(self):
		print(self.name)

	def update_dum_people(self, people):
		dum_people = people

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value
