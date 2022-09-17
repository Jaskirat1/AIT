"""
Logical operators:-

and         |       return Ture if both         |    x =5 and x>5
            |      statements are true          |
            |                                   |
or          |      return True if one the       |   x <5 or x = <4
            |        statements are true        |
            |                                   |
not         |     reverse the result,           |       
            |       return False if the         |   not(x<5 and x<10)
            |         result is true            |  
"""


x = 10
y =20
print(x == 10 and x<y and x == y)           #False   if any statement is false

print( x != 10 or x<y or x == y)           #True     if any statement is true

print(not x != 10)                          #True