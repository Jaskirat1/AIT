#sum 
num = int(input("Enter a number:-"))
print("List of all numbers is :-")
i = 0
list=[]
while i in range(0,num):
    i += 1
    list.append(i)
    r = sum(list)
print(list)
print("sum is:-", r)

    
    