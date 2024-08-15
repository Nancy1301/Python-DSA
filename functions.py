# Functions:

def sum(a, b):
    c = a + b
    # return c # This will return the value and woud be printed
    print(c) # this will print and if we only call the function, it will give the expected value.
    # pass # when we dont want anything to be returned or printed

# print(sum(2,3)) # this will give output when we return from the function.
sum(2,3) # this will give output when we put print statement in the function.


# ------------------------------------- X ------------------------------------- 



# EXAMPLE 1:

def add(lst):
    print(id(lst)) # same id

lst = [1,2,3,4]
print(id(lst)) # same id
add(lst)



# ------------------------------------- X ------------------------------------- 



# EXAMPLE 2:

def add(x):
    print(id(x)) # similar id
    x = 15
    print(id(x)) # diff id because int is immutable so it's creating a new box to store the value but with similar names.

x = 12
print(id(x)) #  similar id
add(x)



# ------------------------------------- X ------------------------------------- 



# EXAMPLE 3:

def add(lst):
    lst.append(5)
    print(id(lst)) # similar id
    lst = [10,12,13,13] # id try to change lst through immutable way
    print(id(lst)) # diff id

lst = [1,2,3,4]
print(id(lst)) # similar id
add(lst)



# ------------------------------------- X ------------------------------------- 



# EXAMPLE 4:

def update(lst):
    n = len(lst)
    print(list(range(n)))
    for i in range(n):
        lst[i] = lst[i]+1

lst = [1,2,3,4,5,6]
print(id(lst)) # this is the address of our original list
update(lst) # Here the list got passed in the function and got updated
print(lst) # the updated list got printed
print(id(lst)) # the updated list's address got printed which is similar to the old ones.

# As we didn't change the list but only updated it and as list is mutable we can change it.




