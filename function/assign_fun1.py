"""
WAP to find the maximum of three numbers.
"""

a= int(input("Enter the value of first number:-"))
b= int(input("Enter the value of second number:-"))
c= int(input("Enter the value of third number:-"))


def first(a,b,c):
    if a>b and a>c:
        print(a, "is biggest number")

    elif b>c and b>a:
        print(b, "is bigger number")

    elif c>a and c>b:
        print(c, "is a bigger number")

first(a,b,c)