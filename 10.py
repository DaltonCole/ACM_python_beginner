from smart import Smart
from dummy import Dummy

dum = Dummy('Sammie')
smarty = Smart('Dalton')

print("People:")
dum.print()
smarty.print()

print("Dum people, smart people:")
print(smarty.dum_people)
print(smarty.smart_people)

print("Value:")
print(smarty.value)
print(dum.value)
print(dum < smarty)


smart1 = Smart('Sara')
smart2 = Smart('Quincy')
smart3 = Smart('Eric')
smart4 = Smart('The other Dalton')
smart5 = Smart('Andrew')
smart6 = Smart('Shawn')


print('Smart people:', smarty.smart_people)
print('Dummy\'s smart people:', dum.smart_people)



'''
class Dummy:
	dum_people = 0
	smart_people = 10

	def __init__(self, name):
		Dummy.dum_people += 1
		Dummy.smart_people -= 1

		self.name = name
		self.value = randint(0,9)

	def print():
		print(self.name)

	def update_dum_people(self, people):
		dum_people = people

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

class Smart < dummy:
	def __init__(self, name):
		Smart.dum_people -= 1
		Smart.smart_people += 1

		self.name = name
		self.value = randint(0,9)

	def update_smart_people(self, people):
		smart_people = people
'''