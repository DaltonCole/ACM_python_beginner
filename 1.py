# Basic syntax - Types

# This is a comment by the way. The python interpreter completely ignores me. Octothorpes scare him.

"""
	Many line comment, even scarier!
"""

# To print:
print("I will print something to the terminal") # Note the (), in < 2.7, you don't need these, in > 3.0, you do.

# If, else, then
if True:
	# Notice the indentation. This represents a new block of code that the if will use
	print("True")
else:
	print("False")

###########################################################
######################### TYPES ###########################
###########################################################

# This is a String variable
string_variable = "hi"

# This is a Numbers variable
numbers_variable = 12345

really_long_number = 1234567890123456789012345678901234567891234567890123456789012345678
really_small_number = .12345678912e-17

# List (array)
list_variable = [1, 2, 3, 'a', 'b', ['string1', "string2"]]

# Tuple
tuple_variable = (1, 2, 3, 'a') # Tuples are like arrays, but immutable

# Dictionary (map in C++)
dictionary_variable = {1: 'a', 'b': 2}
dictionary_variable[3] = "c"


print(string_variable)
print(numbers_variable)
print(really_long_number)
print(really_small_number)
print(list_variable)
print(tuple_variable)
print(dictionary_variable)