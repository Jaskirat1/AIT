"""Add key to dictionary"""

brands = {1:'pepsi', 2:'cola', 3:'gucci'}

# we can updat the value of an item to dictionary using below step:-
brands[1] = "armani"
print(brands)

# we can use update function to add key and value to dictionary

brands.update({5:"brown", 6:"pink"})
print(brands)

#or we can use the below method

brands['x'] = None
print(brands)


# appending the items in dictionary as below:-
brands.update(indigo=7, green =8)
print(brands)

# update the value by assigning values to a variable
var = (('blue',9),('purple',10 ))
brands.update(var)
print(brands)