"""
WAP to make claculate 

"""

num1 = int(input("Enter first number:="))
num2 = int(input("Enter second number:="))
choose = str(input("Enter your choice for :addition, subtraction, division, multiply, modulus, square root:="))

def func(sum, sub, div, mul, mod, sqr):
    if choose == "addition":
        r = num1+num2
        print("Sum is:-", r)
    elif choose == "subtraction":
        r = num1-num2
        print("Subtraction is:-", r)
    elif choose == "division":
        r = num1/num2
        print("division is:-", r)
    elif choose == "multiply":
        r = num1*num2
        print("Multiply is:-", r)
    elif choose == "modulus":
        r = num1 % num2
        print("Modulus is:-", r)
    elif choose == "square root":
        r = num1**2
        print("square root of",num1," is:-", r)

    else:
        print("Invalid input")
    

func("addition", "subtraction", "division","multiply","modulus", "square root")