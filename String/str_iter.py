'''
STRING ITERATION
1.Method

'''
string1 = 'Hello my name is jaskirat'

length = len(string1)   # count total number of character in a string including spaces
print(type(length))

for i in range(length):
    print(string1[i])


print("============================")

for i in range(length-1,-1,-1):     # starting from last character, to end character, decrementby 1
    print(string1[i])