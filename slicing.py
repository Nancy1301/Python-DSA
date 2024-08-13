# SLICING IN STRING & LIST:

name = "Nancy"
print(name[2]) # n

print(name[0:]) # full value gets printed => Nancy
print(name[0:-1]) # the last value is not included => Nanc

print(name[1:]) # ancy 

print(name[1: :2]) # => ac
print(name[-1: :-1]) # reversed


# -------------------------------------------------------------------- X -------------------------------------------------------------------- 



# Updating a character of a string(though it's immutable)

name = "Nanci Bhargava" # needs to change i to y

res = name[0:4] + "y" +name[5:] # Performed slicing and concatenation
print(res)



# -------------------------------------------------------------------- X -------------------------------------------------------------------- 



# Converting string to list

stat = "I love coffee !"
lst = stat.split() # break this
print(lst)

# Converting list to string

col = ["I", "love", "to", "have", "coffees"]
res1 = "Nancy".join(col) # Nancy will be joined with each element of the list and gets converted to string: INancyloveNancytoNancyhaveNancycoffees 
print(res1)
res2 = " ".join(col)
print(res2)




# -------------------------------------------------------------------- X -------------------------------------------------------------------- 


