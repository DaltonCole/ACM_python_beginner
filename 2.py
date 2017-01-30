# Basic syntax - Loops

###########################################################
######################### LOOPS ###########################
###########################################################

i = 0

###################### while loop #########################
print("While: ")
while i < 10:
	print(i, end=', ')
	i += 1
print() # Extra newline


##################### for loop ############################
my_list = [1,2,3,4,5,6]

print("For: ")
# What's going to happen?
for i in my_list:
	print(i, end=', ')
print()


# Range based
for i in range(3):
	print(i, end=', ')
print()

# Ranged based with start and end
for i in range(3, 5):
	print(i, end=', ')
print()

# Ranged based with start, end, and step
for i in range(0, 101, 10):
	print(i, end=', ')
print()


# Ranged with len()
for i in range(len(my_list)):
	print(my_list[i], end=', ')
print()


# Zip
list_a = [1,2,3,4,5]
list_b = ['a','b','c','d']

for a, b in zip(list_a, list_b):
	print(str(a) + ' ' + str(b))
