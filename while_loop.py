'''
While loop and for loop 

syntax for while and for loop 
while(condition):
    statement

#Note:- remember that i++ is not supported by python 


for i in range(condition):
    statement


'''

#Assignment 2 ----> Topic-Loops
#Q1. print first 10 natural numbers

a = int(input("Enter first number to start:"))
for a in range(a, a+10):
    print(a)
    a +=1

"""
while a <= 1:
    

    a += 1 
    print(a)
"""
