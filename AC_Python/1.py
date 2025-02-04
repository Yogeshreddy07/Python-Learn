"""
#>> print function
# print("Hello World")
#print("Yogesh is my name.")
#print("my age is 23")
print("Hii","All")

a=5
b='yogesh'
print(a,b)

#DataTypes  
a=1
b="yogesh"
c=5.003
d=True
print(type(a),type(b),type(c),type(d))
  
a,b,c='yogesh','sem','au'
print(a,b,c)
 
# arithmetic operastor
a= 5
b= 2
sum = a+b
sub= a-b
div=sum/sub
mul=sum*div
mod=a%b
print(sum ,"\n", sub,"\n",div,"\n",mul,"\n",mod)

#Realtional operator
a=5
b=6
print(a==b) #false
print(a!=b) #true
print(a<b)  #true
print(a>b)  #false
print(a<=b) #true
print(a>=b) #false

#type convertion
a= 3
b=5.58888
sum=a+b
print(sum)
s=str(b)
print("string",s,"\n type of data type:",type(s))

#input
name=str(input("enter your name:"))
age=int(input("enter your age:"))
cgpa=float(input("enter your cgpa"))
print(name,"!","welcome to learn coding ","your age is:",age,"your cgpa is:",cgpa)

#sum of two number by taking the input
a=int(input("enter val1:"))
b=int(input("enter val2:"))
sum=a+b
print("the sum is:",sum)
#area of the square
side=int(input("Enter the value os side"))
side*=side
print("the area is:",side)

a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
avg=(a+b)/2
print("the average value is:",avg)
"""
a=int(input("enter the no a:"))
b=int(input("Enter the no b:"))
print(a>=b)