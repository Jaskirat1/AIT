from re import I


num = int(input("Enter a number:="))
fact = 1

for i in range(1,num+1):
     
    fact = fact*i
print("factorial of", num, "is:-", fact)
    