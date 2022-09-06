f = open("file1.txt", "r")
"""
f1 = f.readlines()
for x in f1:
    print(x)

"""
if f.mode == 'r':
    contents = f.read()
    print(contents)