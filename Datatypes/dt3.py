"""
Dictionary:-
is an unordered collection of key-value pairs.
* In python, dictionaries are defined within curly braces{}
with each item being a pair in the form key:value
# same key will not be  defined
mostly used in database
"""

dict = {1:'apple', 2:'pineapple',2:'pineapple'}
print(type(dict), dict)
print(len(dict))

dict[2] ="orange"       #---------Mutable
print(dict)

print(dict[2])



"""
*Set := A set is an unordered collection of items. 
*Every set element is unique (no duplicates) and must be immutable (cannot be changed)
*set is also written in curly braces{}
"""

s ={1, 2,4, 1}
print(type(s), s)
print(len(s))

"""s[2]=3.4 
            ----------> immutable
print(s)"""