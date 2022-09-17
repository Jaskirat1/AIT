"""
WAP which takes a number as a parameter and check the number is prime or not

"""

num = int(input("Enter an input:-"))
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(num))


