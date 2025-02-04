#while loop
"""count=1
while(count<=5):
    print("Hello")  #some work
    count=count+1
print(count)"""
"""i=0
while (i<=5):    
    print("HI",i)
    i+=1
print(i)"""
"""i=1
while(i<=5):
    print(i)  #for the 1-> 5
    i+=1
print("loop ended")"""

"""i=5
while(i>=1):
    print(i)  #for the 5-> 1
    i-=1
print("loop ended")"""
"""i=1
while(i<=100): # 1->100
    print(i)
    i+=1"""
"""i=100
while(i>=1):
    print(i)
    i-=1"""
"""n=0
while(n<=80):
    print( n )
    n=n+8"""
"""i=int(input("enter the number:"))
n=0
while(n<=10):
    print( i,"*",n,"=",i*n )
    n=n+1"""
#trevese
#nums=[1,4,9,16,25,36,49,64,81,100] 
#names=["yogesh","janeesha","subramani","pavithra"]
"""i=0
while (i<len(nums)):
    print(nums[i])
    i+=1"""
"""index=0
while (index<len(names)):
    print(names[index])
    index+=1"""
"""nums=(1,4,9,16,25,36,49,64,81,100)
i=0
x=64
while (i<len(nums)):
    if (nums[i] == x):
        print(nums[i],"is found at index",i)
    else:
        print("finding..")
    i+=1
"""
"""i=1
while i<=5:
    print(i)   
    if(i==3):
        print(i,"is found")
        break
    i+=1
"""
"""list1=[1,2,3,4,5]
for val in list1:       #for the printing of the list
    print(val)"""

"""tup=(1,2,3,4,5,6)
for val in tup:          #for the printing of the tuple
    print(val)
print(type(tup))"""
"""string="yogesh"
for i in string:
    print(i)      #for the printing of the string
print("end")
"""
"""string="yogesh"
for i in string:
    print(i)      #for the printing of the string (using the else condition to print the end)
else:
    print("end")"""
"""num=[1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)
"""
"""num=(1,4,9,16,25,36,49,64,81,100)
x= 81
idx=0
for i in num:
    if(i==x):
        print(i,"is present in the tuple",idx)
    idx+=1"""
"""for i in range(10):
    print(i)
for i in range(1,10):
    print(i)"""

"""for i in range(0,11,2): #(start,end,step up)
    print(i)"""
"""for i in range(1,101):
    print(i)"""
"""for i in range(100,0,-1):
    print(i)"""
"""num=int(input("Enter the num:"))
for i in range(1,11):
    print(i,"*",num,"=",i*num)
"""
"""n=int(input())
sum=0
for i in range(1,n+1,1):
    print(sum,"+",i,"=")
    sum+=i
    print(sum)
print("total sum =",sum)"""

"""n=int(input("enter n:"))
i=1
sum=0
while (i <=n):
    sum += i
    i+=1
    print(sum)"""
n=int(input("enter the number:"))
mul=1
for i in range(1,n+1,1):           #factorial of the number that you enter
    mul=mul*i
    print(mul)

