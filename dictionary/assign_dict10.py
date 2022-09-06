list1 = [1,3,5,2,4]
list2 = ['red','blue','green','orange','pink','purple']

color_dict = dict(zip(list1,list2))
print(color_dict)


max_val = max(color_dict.keys())
print(max_val)
print("-------------")

min_val = min(color_dict.keys())
print(min_val)