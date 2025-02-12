#Write a python function to print multiplication table of a given number. 
def mul(n):
    n=int(input("Enter the mul needed for:"))
    for i in range(1,11):
        print(f"{n} x {i} ={n*i}")
print(mul(2))

