"""
WAP to check wheather a num falls in a given range or not

"""
num = int(input("Enter any number:-"))
def func(a):
    if num in range(1,10):
        print("This is in range")

    else:
        print("This is not in a range!")
func(num)

