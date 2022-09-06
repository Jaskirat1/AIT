import os

"""f = open("practise.txt", "a")
f.write("\nHave a nice day")
f.close()

f = open("practise.txt", "r")
print(f.read())"""

f = open("practise.txt", "w")
f.write("\nThis is write mode.")
f.close()

"""v = open("newfile.txt", "x")"""
"""os.remove("newfile")"""
f = open("practise.txt", "r")
print(f.read())
print("===========")
print(f.tell())
print("==========")
print(f.seek())
print("==========")
print(f.fileno())
if os.path.exists("newfile"):
    os.remove("newfile")

else:
    print("This file does not exists")


"""
os.rmdir("newfolder1")"""

"""print(f.read(10))"""
"""print(f.readline())
print(f.readline())
print(f.readline())"""

"""for x in f:
    print(x)

f.close()"""