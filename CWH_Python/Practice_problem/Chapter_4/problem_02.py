#Write a program to accept marks of 6 students and display them in a sorted manner.


in1=int(input("enter the student marks:"))
in2=int(input("enter the student marks:"))
in3=int(input("enter the student marks:"))
in4=int(input("enter the student marks"))
in5=int(input("enter the student marks:"))
in6=int(input("enter the student marks:"))

marks=[]
marks.append(in1)
marks.append(in2)
marks.append(in3)
marks.append(in4)
marks.append(in5)
marks.append(in6)
print("Marks:",marks) #Marks: [6, 5, 4, 3, 2, 1]
marks.sort()
print("Marks sorted:",marks)#Marks sorted: [1, 2, 3, 4, 5, 6]