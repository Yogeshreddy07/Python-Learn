a=int(input("enter your age:"))

#If statement no:1
if a%2 ==0:
    print("a is even")
#End if statement no:1

#if-elif -else ladder
#If statement no:2
if (a>=18):
    print("can vote")

elif(a<0):
    print("invalid age entered")
else:
    print("can't vote")
#End if statement no:2

print("end of program") #out of the if-elif -else 

# *IMPORTANT NOTES:*
"""1. There can be any number of elif statements. 
2. Last else is executed only if all the conditions inside elifs fail."""

