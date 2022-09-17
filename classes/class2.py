"""class cars:
 
    def __init__(self, name, ctype):
        self.name = name
        self.ctype = ctype
var1 = input("Enter car name:-")
var2 = input("Enter Model:-")




object = cars(var1, var2)
print("Details that you have entered:=",object.name, object.ctype)"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name, abc.age)

p1 = Person("John", 36)
p1.age =40
p1.myfunc()


print("=======================")



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self,name1):
    self.name1 = name1
    print("Hello my name is " + self.name1)

p1 = Person("John", 36)
print(p1.name)
p1.myfunc("kirat")

