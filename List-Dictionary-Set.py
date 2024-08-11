# Data Types:

# String, int, float, boolean
# List -> [] -> list() # Can have duplicates, update: add, delete,
# Tuple -> () -> tuple() # fixed values, can be repeated, can't be updated
# Set -> {} -> set() # Can be changed ; no duplicates ; can update: add, delete
# Dictionary -> {"": value} -> dict() # key-value pair is imp, can be changed/updated
# None


# Operations on data Types:
# These can be performed on String, List, Tuple, Dictionary and Set:

# 1. Getting data
# 2. Adding data
# 3. Removing data
# 4. Updating data

# -> STRING:
# if you have provided string with a value, you cannot change the value but only concatenate or slice it.

fname = "Nancy"
lname = "Bhargava"

name = fname + " " + lname
print(name) # Nancy Bhargava

# -> LIST:

# Have the indexing from 0 itself
# 0,1,2,3,4 ---- indexing
# -3,-2,-1 ----- reverse indexing

lst = [1,2,3,4,5,6,7,8] # can have all data types in the list
print(lst)

lst.append('Nancy') # append is like appending in the end only
lst.append(10.5)
print(lst)

lst.insert(2,"pogo") # inserting means can insert any type of value anywhere and thus, we have to provide index
print(lst)

lst.pop(2) # we have to provide an index
print(lst)

lst.remove(10) # Here we have to provide the value ; if thats not found we will get error
print(lst)
lst.remove(10.5) 
print(lst)

# accessing any value of list

print(lst[-3])

# Updating the values:

lst[0] = 'New Value'
print(lst)

# -> TUPLE:

# Only get data, nothing else:

tup = (1,2,3,4)
print(tup[2])


