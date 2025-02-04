#Concepts of string>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
a="hello"
b="world"
print(a+b)
"""
# for next line we use \n>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
str1="My name is yogesh \ni am in Hosur."
print(str1)
.#for tab space we use \t>>>>>>>>>>>>>>>>>>>>>>>>>>>
str1="My name is yogesh \ti am in Hosur."
print(str1)
# for printing the length of the string>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("the length of the string is:",len(str1))

#indexing
name="yogesh"
print(name[2])
# slicing
name="yogesh"
str1= name[1:4]
str2= name[:4]
str3= name[2:]

print(str1)
print(str2)
print(str3)
#negative indexing
str4= name[-2:-5]
print(str4)

# used to find the endwith
str="i Am Yogesh"
print(str.endswith("a")) #False
print(str.endswith("sh")) #True
# the first word will be capital
print(str.capitalize())
#for replaceing the word
print(str.replace("Yogesh","reddy"))
print(str.find("Yogesh"))  # it will print yhe index of the present word
print(str.find("hi"))# -1 (Not valid) 

str1=str(input("Enter the first name:"))
print(len(str1))
print(str1.find("Yogesh"))

#conditional statement
age=int(input("Enter you age"))
if(age>18):
    print("You  can vote")
else:
    print("You cant vote")
# for calculateing the marks
marks=int(input("Enter Your Marks:"))
if(marks>=90):
    print("grade='A'")
elif(marks>=80 and marks<90):
    print("grade='B'")
elif(marks>=70 and marks<80):
    print("grade='C'")
elif(marks>=60 and marks<70):
    print("grade='D'")

# nesting
age=int(input("Enter the age:"))
if(age>=18):
    if(age<=80):
        print("Can vote..")
    else:
        print("cannot vote the age is above the 80")
else:
    print("Cannot vote the age is below 18")

#user enter the odd or even
num=int(input("Enter the number by the user:"))
if(num/2==0):
    print("its a even number")
else:
    print("its odd number")

num=int(input("Enter the number by the user:"))
if(num/7==0):
    print("divisible by 7")
else:
    print("not divisile by 7")
"""
#finding the greatest of 4 number
num1=int(input("Enter the num 1:"))
num2=int(input("Enter the num 2:"))
num3=int(input("Enter the num 3:"))
num4=int(input("Enter the num 4:"))
if(num1>num2 and num1>num3 and num1>num4):
    print(num1,"num 1 is greater")
elif(num2>num1 and num2>num3 and num2>num4):
    print(num2,"num 2 is greater")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3,"num 3 is greater")
elif(num4>num1 and num4>num2 and num4>num3):
    print(num4,"num 4 is greater")
    