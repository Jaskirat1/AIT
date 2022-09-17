"""
WAP to calculate the factorial of two numbers:"""
#import math



def fact(n):
    facto = 1

    for x in range(2, n+1):
        
        facto = facto*x
    print("The factorial of", num, "is", facto)

num =int(input("Enter input :="))
fact(num)


"""
def factorial(n):
    return 1 if (n ==1 or n==0) else n*factorial(n-1)


num = int(input("Enter input"))
print(factorial(num))"""



"""num = int(input("Enter any input:-"))
def myfact(n):
    return(math.factorial(n))


print(myfact(num))"""