# Strings

###########################################################
####################### STRINGS ###########################
###########################################################

s1 = 'String1'
s2 = "My name is not Bob, thank you very much."

print(s1)

print(s1[2])	# Indexable

print(s1[2:5])	# Slice

print(s1[0:-1:2])

print(s1[-1])

print(s1[0::2])

# For loop
for s in s1:
	print(s, end=' ')

print('\n')

print((s1 + ' ') * 5)

if 'S' in s1:
	print('Do the Nay Nay')

if 'S' not in s1:
	print('')

print('This is a string:', s1)

# Unicode 
print(u'Unicode fun?')
print(u'\uFB41')

# Binary string
print(b'hi')


# Fun functions

print('jonny boy'.capitalize())
print('hello, this is a string with some number of hs in it'.count('h')) # 4
print('this is a sentence.'.find('s')) # 3
print('hi123'.isalpha()) # False
print('hi123'.isalnum()) # True
print('123'.isdigit()) # True
print(len('Bob the builder')) # 14
print('My name is Dalton Cole and I am really cool, Dalton Cole!'.replace('Dalton Cole', 'Sara Newman'))
print('JoHn Is A pErSoN tO bE kNoWn'.swapcase())



