"""#for loops
#list
l=[1,3,2,4,5]
for i in l:
    print(i)

#tuple
l={1,3,2,4,5}
for i in l:
    print(i)

#strings
name="yogesh"
for i in name:
    print(i)"""  

#For loop with else
l=[1,3,2,4,5]
for i in l:
    print(i)
else:
    print("end")

#break funciton
for i in range(1,11):
    if i ==3:
        break #exits the loop right now
    print(i)
"""
1
2
"""

#continue
for i in range(1,11):
    if i ==3:
        continue #it skips the condition so 3 will not be printed
    print(i)

#pass -> it instructs to “do nothing”.
for i in range(220):
    pass  # without pass, the program will throw an error 