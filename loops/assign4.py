#Q4. print table of any number

num = int(input("Table of:"))
"""i = 1
while i <=10:
    mul =num*i  
    i+=1
    print(mul)
"""
i = 0
for i in range(0,10):

     i +=1
     mul = num*i
     print( num,"*",i,"=",mul)