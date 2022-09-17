"""type casting 
int
float
str
eval"""

a = input("Enter your first name:-")
b = input("Enter your last name:-")

print(a+" "+b)

a  = int(input("Enter first number:="))
b  = int(input("Enter second number:="))

print(a+b)

a  = float(input("Enter first number:="))
b  = float(input("Enter second number:="))
print(a+b)

print("-------------")
a  = eval(input("Enter first number:="))
b  = eval(input("Enter second number:="))
print(a+b)


eval = eval(input("Enter any number:="))
print(eval)
print(type(eval))


x = input("Enter any expression:=")
y = eval(x)
print("The result is ",y)