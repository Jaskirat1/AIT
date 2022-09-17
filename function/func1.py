def func(name):
    """
    this is a doctstring.
    
    """
    print("hello my name is " ,name)

print(func("kirat"))

print(func.__doc__)
print(func("Jaskirat"))

"""
if there is no expression in the statement or 
the return statement itself is not present inside a function, then the function 
will return th None object.
"""