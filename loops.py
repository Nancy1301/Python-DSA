# CONDITIONAL STATEMENTS AND LOOPS:

# Indentation is IMP
# There is NO SWITCH STATEMENT IN PYTHON

# marks = int(input())

# if marks>=90:
#     print("A")
# elif marks>=50:
#     print("B")
# else:
#     print("C")

 
# -------------------------------------------------- X -------------------------------------------------- 



# LOOPS:- 1. While ||  2. For

pushup = 0 # initialization 
while pushup<5: # condition
    print("do more") # operation
    pushup = pushup+1 # updation


# range():

print(range(1,4))
print(list(range(1,4))) # wants to give a sequence 4 wouldn't be considered
print(list(range(1,10,2))) # works like a slicing only



for name in range(10): # sequence is range() or list or anything and i is variable name
    print("nancy") #operation

for num in range(1,11):
    print (num)

#  Printing list's value and it's index => enumerate()

lst = ["Nancy", "loves", "coffee"]

n = len(lst)

# Two ways:

for index,value in enumerate(lst):
    print (index, "-", value)

for index in range(n):
    print (index, "-", lst[index])


# -------------------------------------------------- X -------------------------------------------------- 
