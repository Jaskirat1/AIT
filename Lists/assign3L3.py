#Qus3. ------>
#write python function which takes two lists
# return true if the lists have common value

Li1 = [1,2,3,4,7]
Li2 = [1.3,5,6]



def func(args, args2):
    for i in args:
        for j in args2:
            if i == j:
                print("True") 
            else:
                return False
func(Li1, Li2)

