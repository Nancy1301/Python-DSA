# INPUT, OUTPUT and DATA TYPES

print("Hello")

x = 5
print(x)

print(x,"is a number")

y = 8
print(x) # in print function by default it has a "\" space added and thats why it prints in the next line.
print(y) 

z = "Space is there."
print(3,z, end="-") # end basically changes the default function as per mentioned task in it.
print(5)

# Taking Input

name = input()
print(name)

age = input()
print(type(age)) 

age = int(input()) # converting the input to int and this can be done with other data types as well.
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
