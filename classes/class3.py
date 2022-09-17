"""

Methods :=Bsically , methods are the functions defining 
inside a class that tells the behaviour of an object.

"""

class cloths:

    cloth_type = "is not chiffon"
    cloth_type2 = "is a crepe"

    def __init__(self, febric, size):
        self.febric = febric
        self.size = size
    
    def good(self, msg):
        print("this is a good febric {}".format(msg))

    def bad(self,msg):
        print("{} {}".format(self.febric,msg))


object = cloths("Cotton", "XXL")
object2 = cloths("crepe", "XL")


# access the instance attributes:-

print("cloth is of {} type".format(object.febric, object.size))
print("cloth is of {} type".format(object2.febric, object2.size))


#access the class attribute 


print("cloth type {}".format(object.__class__.cloth_type))
print("cloth type {}".format(object.__class__.cloth_type2))


#call methods:-
print(object.good("Thank you"))
print(object2.bad("is not a good febric"))
