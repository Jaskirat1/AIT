"""
Membership operators

in          ======>  returns True if a squence with the specified value is present in th object ====> x in y 
not in      ======>  return True if a sequence with the specified value is not present in the object ====> x not in y

"""

x ="Hello"

print('h' in x)     #False
print('H' in x)     #True

print('t' not in x)     #True
print('ll' not in x)    #False

print("=========")
list1 = [10,30,423,24]
print(20 in list1)


dict = {1:23, 2:"helo", 3:324}
print('h' in dict)