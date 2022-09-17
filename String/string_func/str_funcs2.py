'''
Python functions :-
1.find() ---> to find character on which it is
2.index() --->to find indexing of a letter
3.isalpha --->if only alphabets is availabe it gives true else false
4.isdigit() --->if only digits then true else false
5.isalnum() --->if num or character then true else false

'''

#1. Find()

w = 'My name is Jaskirat'
a = 'Hello'
b = '12345566'
c = '123ABC '
d= '-123123'
print(w.find('t', 1))       # here 2 is indexing number starting from 2 
#print(w.find('z'))    ---> output is -1 coz that letter is not in string
print("==============")

print(w.index('r', 3))
#print(w.index('z', 3))     ------> output will be an error 
print("==============")


print(w.isalpha())
print(a.isalpha())
print("==============")


print(b.isdigit())

print("==============")

print(b.isalnum())
print(c.isalnum())          # space is also gives an error
print(d.isalnum())          #---> False




