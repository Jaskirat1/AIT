"""
Task 2 ---------Print grade of a student-----------
"""



name = input("Enter the name of student:")

if name == "Simran":
    student1 = {'English': 75,'Punjabi':85,'Math':88,'Science':79}
    sum_of_marks = student1.values() 
    print(student1)
    print(sum_of_marks)    #prints------> Dict_values
    addition = sum(sum_of_marks)
    print("Total marks obtainted by Simran:",addition)         #prints========> Total marks obtainted!
    Total = addition/400 * 100
    print("Percentage:=",Total)


    if Total >= 90:
        print("Grade A")

    elif(75 <= Total >= 85):
        print("Grade B")

    elif Total <= 60:
        print("Grade C")



elif name == "Aman":
    student2 = {'English': 65,'Punjabi':45,'Math':75,'Science':66}
    sum_of_marks = student2.values()
    print(student2)
    print(sum_of_marks)
    addition = sum(sum_of_marks)
    print("Total marks obtainted by Aman:",addition)         #prints========> Total marks obtainted!
    Total = addition/400 * 100
    print("Percentage:=",Total)


    if Total >= 90:
        print("Grade A")

    elif(Total >= 60):
        print("Grade B")

    elif Total <= 60:
        print("Grade C")


    
elif name == "Kiran":
    student3 = {'English': 95,'Punjabi':91,'Math':92,'Science':90}
    sum_of_marks = student3.values()
    print(student3)
    print(sum_of_marks)
    addition = sum(sum_of_marks)
    print("Total marks obtainted by Kiran:",addition)         #prints========> Total marks obtainted!
    Total = addition/400 * 100
    print("Percentage:=",Total)


    if Total >= 90:
        print("Grade A")

    elif(75 <= Total >= 85):
        print("Grade B")

    elif Total <= 60:
        print("Grade C")

