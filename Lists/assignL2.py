#Ques.7 ----------->
#Clone or copy a list 

import copy
l = [1,1,2,3,4,5,4]

l2 = l.copy()
print(l2)

l2 = [1,4,5,6,6,[2,3]]
new_list =l2
print(new_list)

l3 = ['name', 1, 3.4]
list3 = l3[:]
print(list3)

list3.append('Pyhton')
print(list3)

list3.extend(l2)
print(list3)

#shallow copy

list1= copy.deepcopy(l2)
print(list1)