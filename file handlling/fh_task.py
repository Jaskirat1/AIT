#task regarding file handling

print("Hello user!")
choose = input("To edit, read or write in file.txt choose any mode w/r/a :-")

if choose == "w":
        
    var= open("file.txt", "w")
    topic = input("Topic name:-\n")
    var.write(topic)
    content = input("\nContent:- \n")
    a = input("Do you want to write more content more?yes/no?")
    
    if a == "yes":

        var= open("file.txt", "w")
        
        content = input("\n Enter the content:- \n")       
        var.write(content)
        print(var)
        var.close()
    else:
        print("thanks")
       
elif choose == "r":
    var= open("file.txt", "r")
    x = var.readlines()
    print(x)
    var.close()
    
    """content = var.read()
    print(content)"""


elif choose == "a":
    
    var= open("file.txt", "a")
    topic = input("Topic name:-\n")
    content = input("\n Enter the content:- \n\n")
    var.write(topic)
    var.write(content)
    var.close() 
   
else:
    print("Invalid input")
