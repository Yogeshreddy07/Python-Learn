#Functions:
"""A function is a group of statements performing a specific task. 
When a program gets bigger in size and its complexity grows, it gets difficult for a 
program to keep track on which piece of code is doing what! """

#funtion definition
def avg():
    a=int(input("Enter your number:"))
    b=int(input("Enter your number:"))
    c=int(input("Enter your number:"))
    average=(a+b+c)/3
    print(average)
#funtion call
avg()
avg()

def goodday():
    inq=input("enter the user name:")
    print(f"{inq}!,Good Day")

goodday()

#function with arguments
def good(name,ending):
    print(f"good day {name}!")
    print(ending)
good("yogesh","thanks")
good("reddy","thank you")

#default arguments
def goods(name,end="thank you"):
    print(f"good day {name}")
    print(end)
goods("yogesh") #if the arguments are not give also it thake the defalt thats given.
goods("yogesh","tk") #if the argument are given the the arguments will be changed by given

#return A function can also return value as shown below:
def re(name):
    gr="hello "+ name
    return gr
a=re("yogesh")
print(a)



