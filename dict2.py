dict1 = { 1:2, 2:4, 3:6}
print(dict1)
dict1[2] = 40
print(dict1)
dict1.update({3:60})
print(dict1)
for x,y in dict1.items():
    print("key", x, ": value", y)