#File handling

"""
there are 3 modes in file handling
1. read
2. write
3. append


#program, how to create a file and write something in it :=
"""
a = open("file1.txt", "w")
a.write("Hello kirat \n")
a.close()


a= open("file1.txt", "a")
a.write("Python \n")
a.close()

'''
a = open("kirat.txt", "w")
a.write("Hello kirat")
a.close()


a= open("kirat.txt", "a")
a.write("Python")
a.close()'''
