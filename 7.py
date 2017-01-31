a = 'a'

try:
	print(a)
except:
	print('Hit Except')
else:
	print('Else')
finally:
	print('Finally')


print('del a', end='\n\n')
del a

try:
	print(a)
except:
	print('Hit Except')
else:
	print('Else')
finally:
	print('Finally')