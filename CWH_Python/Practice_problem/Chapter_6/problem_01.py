#Write a program to find the greatest of four numbers entered by the user.
l=[]
s=int(input("enter the num:"))
l.append(s)
s=int(input("enter the num:"))
l.append(s)
s=int(input("enter the num:"))
l.append(s)
s=int(input("enter the num:"))
l.append(s)
print(l)
if(l[0]>l[1] and l[0]>l[2] and l[0]>l[3] ):
    print("a is greater:",l[0])
elif(l[1]>l[0] and l[1]>l[2] and l[1]>l[3] ):
    print("b is greater:",l[1])
elif(l[2]>l[1] and l[2]>l[0] and l[2]>l[3] ):
    print("c is greater:",l[2])
elif(l[3]>l[1] and l[3]>l[2] and l[3]>l[0] ):
    print("d is greater:",l[3])