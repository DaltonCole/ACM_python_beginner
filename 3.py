# Numbers

import math
from math import pi
from math import e as natural_number

###########################################################
####################### NUMBERS ###########################
###########################################################

# del deleates the reference to a number object
a = 3
print(a)

del a
#print(a) # Error

# signed int
i = 10

# Float
f = 12.12

# Complex
c = 12 + 2.2j


## Conversion

print(int(f))

print(float(i))

print(complex(i)) # real = 10, complex = 0
print((complex(i, .3) + c))


## Funtions

print("------------------------")

print(abs(-10)) # 10

print(math.ceil(12.2)) # 12

print(pow(2, 4)) # 16

print(pow(2, 4, 3)) # 2^4 % 3 = 1

print(math.sqrt(4)) # 2.0

print(math.sin(.789)) # 0.7096490720426565

print(pi)

print(natural_number)