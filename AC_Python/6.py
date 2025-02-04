#function
"""def sum(a,b): #parameters
    sum = a+b
    return sum #store the value

print("the sum of 4 And 5 is",sum(4,5))"""
"""def calculate(a,b):
    return a + b
sum=calculate(2,3) #function call , ()->funtion arguments
print(sum)"""
"""def print_hello():
    print("hello")
print_hello()"""
"""def avg(a,b,c):
    avg1=(a+b+c)/3
    return avg1
print(avg(1,2,3))
"""
"""a = ["a","b","c","d"]
def li(a):
    b=len(a)
    return a ,b
print(li(a))"""
"""a = ["a","b","c","d"]
b = ["a","b","c","d","c"]
def functionlen (list):
    a=len(list)
    return a
print(functionlen(a))
print(functionlen(b))"""
"""a = ["a","b","c","d"]
b = ["a","b","c","d","c"]
def print1(list):
    for i in list:
        print(i,end=" ")

print(print1(a))
print(print1(b))"""
"""def fact1(n):
    fact=1
    for i i8n range(1,n+1,1):
        fact*=i
    print(fact)
print(fact1(5))"""
"""def usd2inr(usd):
    inr=usd*86
    print("usd=",usd,"inr=",inr)
usd2inr(10)"""
"""num=int(input())
def oddeven(number):
    if ((number/2) != 0 ):
        print("odd")
    elif((number/2) == 0):
        print("even")
    
oddeven(num)"""
"""#recursive function
num=int(input("Enter the number:"))
def pr(num1):
    if (num1==0):
        return
    print(num1)
    pr(num1-1)
pr(num)
    """
"""for i in range(5,0,-1):
    print("*"*i)
"""
"""def show(n):
    if(n==0):
        return
    print("*"*n)
    show(n-1)
    print("end")
show(5)"""
"""def rec(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * rec(n-1)
        rec(n-1)
print(rec(5))"""
"""def sum(num):
    sum=0
    for i in range(1,num+1,1):
        sum+=i
        print(sum)
sum(10)"""
def pr(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    pr(list,idx+1)
n=[1,2,3,4,5,6]
pr(n,1)


