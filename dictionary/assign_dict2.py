#Concatenate and merge two dictionaries

dict1 = { 1: "apple", 2: "mango", 3:"orange"}
dict2 = { 4:"red", 5:"yellow", 6:"orange"}

dict3 = dict1 | dict2
dict1.update(dict2)

print(dict3)
print(dict1)

