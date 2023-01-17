
r=int(input(""Input the radius of the circle:""))
area = (22/7)*r*r
print("the area of the circle is:")
============================================================================
import os
filename=input("enter filename: ")
filename,file_extension=os.path.splitext(filename)
print("file_extension==",file_extension)
if(file_extension=='.py'):
    print("Its python program file")
elif(file_extension==".txt"):
    print("Its a text file")
elif(file_extension==".c"):
    print("Its a c program file")
elif(file_extension==".cpp"):
    print("Its a c++ program file")
elif(file_extension==".java"):
    print("Its a java program file")
=============================================================================
