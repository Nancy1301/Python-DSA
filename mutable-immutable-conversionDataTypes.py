# Mutable -> something that can be changed
# Examples: List, Dictionary, Set, User-Defined Classes

# Immutable -> something that cannot be changed
# Examples: int, float, bool, string, tuple


x = 5
print(id(x))
x = 10
print(id(x)) # the x value would update from 5 to 10 BUT the address would change therefore they aren't identical. 

y = 5
print(id(y))
x = 5
print(id(x)) # In this case, it will have same address due to same values

# THIS IS THE SMARTNESS OF PYTHON AS IT SAVES A LOT OF SPACE.

# -------------------------------------- X --------------------------------------

# CONVERSION B/W DATA TYPES:

# Condition -> that should be valid eg: converting "hello" to int doesn't make any sense.

# eg 2: converting list/tuple/set to dictionary doesn't make sense as there isn't any key-value pair
# eg 3: True/False can be 1/0 but not -5/5

# convert in what ? eg: float to int -> int(value of float)

a = 4.5
print(a, type(a))

res = int(a)
print(res, type(res))

res1 = str(a)
print(res1, type(res1))

lst = [ 1,2,3,4 ]
print(lst, type(lst))

res2 = tuple(lst)
print(res2, type(res2))

res3 = set(lst)
print(res3, type(res3))

color = [ "blue", "pink", "black" ]
quantity = [1,2,3]
# creating a dictionary out of these 2 lists:

res4 = zip(color,quantity)
print(res4, type(res4)) # can't see this zip and needs to be converted to dict
res4 = dict(res4)
print(res4, type(res4))

# Converting to bool


# This will give False because there is no value, it's all empty:
print(bool([]), bool(()), bool({}), bool(""), bool(0), bool(0.0))

# Now, if there is a value
print(bool([3]), bool((4)), bool({}), bool(""), bool(1), bool(0.0))

res5 = (5) # This should be a tuple but it comes out to be an int value because as per python, it understands that this is just brackets for an arithmetic operation
print(res5, type(res5))

res6 = (5, ) # This makes python understand that it would be having values and it's a tuple 
print(res6, type(res6))

# zip -> object type that we can't print or see ; we have to convert it into some other data type


# Uses:

# 1. For Unique elements: convert into set and for result convert back to list
# 2. Zip only converts to dictionary because it uses 2 diff data types and forms 1
