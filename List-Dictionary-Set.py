# Data Types:

# String, int, float, boolean
# List -> [] -> list() # Can have duplicates, update: add, delete,
# Tuple -> () -> tuple() # fixed values, can be repeated, can't be updated
# Dictionary -> {"": value} -> dict() # key-value pair is imp, can be changed/updated
# Set -> {} -> set() # Can be changed ; no duplicates ; can update: add, delete=
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


# ----------------------------------- XXXXX ----------------------------------



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

# lst.remove(10) # Here we have to provide the value ; if thats not found we will get error
# print(lst)
lst.remove(10.5) 
print(lst)

# accessing any value of list

print(lst[-3])

# Updating the values:

lst[0] = 'New Value'
print(lst)



# ----------------------------------- XXXXX ----------------------------------




# -> TUPLE:
# Only get data, nothing else:
tup = (1,2,3,4)
print(tup[2])



# ----------------------------------- XXXXX ----------------------------------




# -> Dictionary:

# unique keys only, values can be duplicates though
# efficient in case of time
# no indexing required
# no ordering

dct = {"nancy":24, "gunnu": 19, "shekhar": 26, "ashu": 26} # key-value pair
print(dct['gunnu'])

dct['gunnu'] = 20  # updated the value
print(dct)

dct['kashish'] = 23 # adding a value
print(dct)

# If we access any value which is not present, we'll get an error

dct.get("fruit", "orange") # get function would give a default value if the key is not present in the dictionary
print(dct.get("fruit", "orange")) # as fruit is not present, so it will give orange value
print(dct.get("nancy", "orange")) # as nancy is present so it will gove age value 24 as output

# deleting a value

del dct["kashish"]
print(dct)




# ----------------------------------- XXXXX ----------------------------------




# -> Set:

# uniques items only
# efficient in case of time
# no order, no numbering


st = {} # this is by default a dictionary, but if we give a single value it would be considered as set.
st = set() # creating empty set 

st = {1,2,3,4}

# st[0] # can't do this as it's not ordered
# To check if there is a value present in set:

# val in st -> would give True or False
print(3 in st) # return true
print(10 in st) # return false

# Adding values:

st.add(3) 
print(st) # In this case, as 3 is already there in the set it wont add again and print the same set

st.add(5)
print(st) # Here it will add 5 in the set

# As there is no concept of index, set is unordered we can't do append or insert functions because they apply as per indexing rule.

# Removing values:

st.remove(2)
#st.remove(7) # would give error as it's not in the set
print(st)

# Getting length:

print(len(st))

# Initialising empty variables:

name = " "
age = 0
lst = []
tup = ()
dct = {}
set = set()


# ----------------------------------- XXXXX ----------------------------------