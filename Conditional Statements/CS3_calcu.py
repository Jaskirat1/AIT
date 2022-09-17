print('''
+ Add
- Subtract
* Multiply
/ Divide
''')

num1 = int(input("Enter first number:="))
num2 = int(input("Enter second number:="))
opr = input("Enter any operator +, -, *, / :=")

if opr =='+':
    print(num1+num2)
elif opr =='-':
    print(num1-num2)

elif opr =='*':
    print(num1*num2)
elif opr =='/':
    print(num1/num2)
if opr != '+' and opr != '-' and opr != '*' and opr != '/':
#else:
    print("Invaild operation")

