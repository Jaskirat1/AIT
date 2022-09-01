num =int(input("Enter a number:-"))
num = int(repr(num)[-1])
print(num)

if num/3 == 0:
    print("Last digit is divisible by 3")

else:
    print("Last digit is not divisible by 3")


