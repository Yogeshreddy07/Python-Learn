#Write a program to print multiplication table of n using for loops in reversed order.
n=int(input("enter the number:"))
for i in range(10,0,-1):
    print(f"{n} x {i} = {n*i}")
     