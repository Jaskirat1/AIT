"""
Bitwise operators 

&       | AND   | x &y

|       | OR    | x|y

^       | XOR   | X^y
-----------------------------------------------------------
1 = true   / 0 = False
----------------------
A       B           A&B         A|B         A^B
0       0           0            0           0
0       1           0            1           1   
1       0           0            1           1   
1       1           1            1           0

XOR = if both are same i.e 0 0 =0 or 1 1 = 0 then False otherwise True means if any one is true the true.
"""
x = 10 
y =8 

print(bin(10))
print(bin(8))
print("=======")

print(bin(x&y), x&y, y&x)

print(bin(x|y), x|y)

print(bin(x^y), x^y)
