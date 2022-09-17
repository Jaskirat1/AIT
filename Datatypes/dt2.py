"""
Sequence datatype:=
*string
*List
*tuple

string is a collection of one or more characters put in a single quote, double -quote or triple quote
multi-line strings can be denoted as ''' ''' or """ """ also used for comments

"""

s = "My name is Jaskirat "
print(s)
s = 'Hello Kirat'
print(s)

s = '''
    hello
    welcome to python world
'''

print(s)
"""
s[1] ='H'     ----------------------> Immutable
print(s)"""


s = '10'
print(type(s), s)



print("---------------------------------------")

"""
List mutable datatype
~List is an  ordered sequence of items.
~It is one of the most used datatype in python and is very flexible 
~written in []


"""

a = [1,2,'hello']
print(type(a), a)
print(len(a))
a[0]=5.5    #------ list is mutable
print(a)


"""
Tuple is an ordered sequence of items same as list.
Tuple is immutable datatype.
it is defined within parathese() where items are separated by commas.
we can access tuple fast than list

"""
t =( 2, 'hello', 3.4, 0, 3+4j)
print(type(t), t)
print(len(t))

"""t[0] =3      
                    ------ tuple is immutable
print(t)"""

t =(2.3)
print(type(t))

print("-----------------------------")

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