f_val = int(input("Enter first lower value:-"))
l_val = int(input("Enter last value:-"))


for num in range(f_val, l_val+1):
    if num >1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:

            print(num, end =" ")

