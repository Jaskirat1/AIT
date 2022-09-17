#Qus.1
#sum of all items
List1 = [1,24,5,7,8]

print(sum(List1))

#Qus2. ------>
#multiply all items
List = [1, 2, 3 , 4]
i = 1
for i in List:
    print(i*2)


#Qus3. ------>
#maximum number from a list
List = [1,2,3,4 ,55]

print(max(List))

#Qus4. ----->
#minimum number from a list

print(min(List))

#Ques.5 --->
#check list is empty or not

List2=[1, 2, 3, 5, 6, 7]
List3=[]

if len(List2)== 0:
    print("List is not empty")

else:
    print("List has items")

print("---------------")
print(len(List2))
print(len(List3))

#Ques.6 ----------->
# remove duplicates
l = [1,1,2,3,4,5,4]

print(*set(l))


print(list(set(l)))




