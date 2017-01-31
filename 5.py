# Lists

###########################################################
######################### Lists ###########################
###########################################################

l1 = [1, 2, 3, 4, 5, 6, 7, 'a' , 'Johnny Boy']

print(l1) # [1, 2, 3, 4, 5, 6, 7, 'a', 'Johnny Boy']

# Remove element
del l1[5]

print(l1) # [1, 2, 3, 4, 5, 7, 'a', 'Johnny Boy']

# length
print(len(l1)) # 8

# Concatenate
print([1,2,3] + [5,6,7]) # [1, 2, 3, 5, 6, 7]

# Repitition
print(['John'] * 5) # ['John', 'John', 'John', 'John', 'John']

# In
print(6 in l1) # False

# Iteration
for x in [1,2,3]: print(x, end=' ')
print()


# Indexing
l1[2] # 3

l1[-2] # 'a'


# Functions
l2 = ['a', 'b', 'c']
print(max(l2)) # c
print(min(l2)) # a
l3 = list((1, 2, 3)) # Tuple to list

l1.append(l2) # [1, 2, 3, 4, 5, 7, 'a', 'Johnny Boy', ['a', 'b', 'c']]
