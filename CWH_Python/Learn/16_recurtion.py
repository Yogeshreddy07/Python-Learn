def factorial(n):
    if(n==1 or n==0):
        return 1
    return (n * factorial(n-1))

n= int(input("enter a number:"))
print(f"the factorial of {n}= {factorial(5)}")
factorial(5) #note if you aren using return you have to print the funtion

