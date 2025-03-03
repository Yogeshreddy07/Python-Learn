#Write a program to find whether a given number is prime or not.
n=int(input("Enter the number:"))
for i in range(2,n):
    if(n%i==0):
        print("Not a prime",n)
        break
else:
    print("Number is prime")