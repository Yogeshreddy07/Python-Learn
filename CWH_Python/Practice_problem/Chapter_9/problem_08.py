"""
Write a program to print the following star pattern. 
  * 
 *** 
***** for n = 3
"""
n=int(input("Enter the n value:"))
for i in range(1,n+1):
    for j in range(n+1,i+1,-1):
        print(" ",end=" ")
    for j in range(i-1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    print("* "*(2*i-1),end=" ")
    print("")
             
 