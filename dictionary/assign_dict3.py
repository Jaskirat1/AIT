dict1 ={1: 'apple', 2: 'mango', 3: 'orange', 4: 'red', 5: 'yellow', 6: 'orange'} 

num =int(input("Enter a key to check :-"))

if num<=5:
    num =dict1.keys()
    num2 = dict1.values()
    print(num,"key is available")
    print(num2)
else:
    print("This key is not available.")