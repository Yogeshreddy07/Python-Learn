#Write a program using functions to find greatest of three numbers.
def great(a,b,c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>b and c>a):
        return c
print(f"the greatest number is:{great(2,3,1)}")