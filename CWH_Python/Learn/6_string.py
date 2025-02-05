#intro to string
name="""yogesh"""
name1="yogesh"
name2='yogesh'
n=len(name)#for finding the length of the string

#STRING SLICING 
n1=name[0:3]# start from index 0 all the way till 3(excluding 3)
print(n)

#negative slicing
n2=name[-4:-1]
print(n2)
print(name[:]) #used to print full string (yogesh)
print(name[:4]) #used to print from index 0->3 (yoge)
print(name[1:]) #used to print from index 1->5 (ogeh)

#skip value
print(name[1:6:2])
a="123456789"
print(a[0:9:3]) #jumps by 3 (147)


