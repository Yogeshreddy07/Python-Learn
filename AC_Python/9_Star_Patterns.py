#star patterns
n=int(input("enter the number:")) #5

for i in range (1,n+1):
    for j in range(1,n+1,1):
        print("*",end=" ")
    print("") 
print("\n")
"""
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range (1,n+1):
    for j in range(1,i+1,1):  # i+1
        print("*",end=" ")
    print("")
print("\n")
"""
*
* *
* * *
* * * *
* * * * * 
"""

for i in range (n,0,-1):
    for j in range(i,0,-1):  #i
        print("*",end=" ")
    print("")
print("\n")
"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range (1,n+1):
    for j in range(1,i+1,1):
        print(j,end=" ")        
    print("")
print("\n")
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
"""

for i in range (n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")        
    print("")
print("\n")
"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
for i in range(1,n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
print("\n")
"""
      *
    * *
  * * *
* * * *
""" 
for i in range(1,n):
    for j in range(i-1,n-1):
        print(" ",end=" ")
    for j in range(i-1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

    """ * 
      * * *
    * * * * *
  * * * * * * *"""
print("\n")


for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(i,n+1):
        print("*",end=" ")
    for j in range(i+1,n+1):
        print("*",end=" ")
    print()
"""* * * * * * * * *
     * * * * * * * 
       * * * * *
         * * *
           *"""
print("\n")

for i in range(1,n):
    for j in range(i-1,n-1):
        print(" ",end=" ")
    for j in range(i-1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(i,n+1):
        print("*",end=" ")
    for j in range(i+1,n+1):
        print("*",end=" ")
    print() 
"""
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
"""
