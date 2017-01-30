from random import randint

def func1():
	return 'hi'

def func2(x):
	return x ** 2

def func3(x):
	return x // 2

def func4(x, y=6, z=10):
	return x + y + z

def func5(x):
	x = 'Pass by reference'

def func6(y):
	y.append(['hey', 'now'])

def func7(y,z):
	print(y + z)

def variable_length_argument_function(a, *b):
	print(a)
	for i in b:
		print(i, end=' ')
	print()

def func8(text):
	return [ord(c) for c in text]

def func9():
	return lambda a, b: a+b

def func10():
	x = randint(0,9)
	if x < 5:
		pass
	elif x == 6:
		print('hi')
	else:
		print('else')


if __name__ == '__main__':
	print(func1())  # hi
	print(func2(3)) # 9
	print(func3(9)) # 4
	print(func4(2)) # 18
	print(func4(3,4)) # 17

	x = 10
	func5(x)
	print(x) # 10, this is because the paramater becomes local in function because of reference change

	y = ['a', 2]
	func6(y)
	print(y) # ['a', 2, ['hey', 'now']]

	func7(z = 'a', y = 'b')

	variable_length_argument_function(1, 2, 3, 4, 5)

	# lambda
	sum_lambda = lambda a, b: a + b

	print(sum_lambda(1, 4))

	sum2_lambda = lambda a, *b:  [a] + list(b)

	print(sum2_lambda(1, 2, 3, 4, 5)) # [1, 2, 3, 4, 5]

	print(func8('Dalton is Cool')) # [68, 97, 108, 116, 111, 110, 32, 105, 115, 32, 67, 111, 111, 108]

	a = func9()
	print(type(a)) # <class 'function'>
	print(a(1,2)) # 3

	func10()