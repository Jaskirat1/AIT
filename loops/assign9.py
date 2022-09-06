num = int(input("Enter the Range Number: "))
First_val = 0
Second_val = 1
for n in range(0, num):
           if(n <= 1):
                      next = n
           else:
                      next = First_val + Second_val
                      First_val = Second_val
                      Second_val = next
           print(next)

            