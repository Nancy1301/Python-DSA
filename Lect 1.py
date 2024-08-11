# INPUT and DATA TYPES

print("Hello")

x = 5
print(x)

print(x,"is a number")

y = 8
print(x)
print(y) # print by default has a space to let it start from next line.

z = "Space is there."
print(3,z, end="-") # now by default it wont print a new line
print(5)

# Taking Input

name = input()
print(name)

age = input()
print(type(age)) 

age = int(input()) # lets convert the input to int
print(type(age))

# Taking input for multiple types in one row

a,b,c = map(int, input().split()) # split function is breaking the specific input
print(a,b,c)

# When a lot of input values, then it's best to use List 

lst = map(int, input().split())

# Converting to list data type

lst = list(map(int, input().split()))
print(lst)

print(len(lst))

# Data Types:

# String, int, float, boolean
# Set -> {} -> set() # Can be changed ; no duplicates ; can update: add, delete
# List -> [] -> list() # Can have duplicates, update: add, delete,
# Tuple -> () -> tuple() # fixed values, can be repeated, can't be updated
# Dictionary -> {"": value} -> dict() # key-value pair is imp, can be changed/updated
# None


# Operations on data Types:
# These can be performed on String, List, Tuple, Dictionary and Set:

# 1. Getting data
# 2. Adding data
# 3. Removing data
# 4. Updating data