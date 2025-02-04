"""f=open("7.txt","r") #r for read
#data=f.read()
data1=f.readline()
#print(data)
print(data1)
print(type(data1))
f.close()"""
"""f=open("7.txt","a")  #a -> upend, w-> write
data=f.write("i want to learn java for DSA from tomorrow.")
print(data)
f.close"""
"""with open("7.txt") as f:
    data=f.read()
    print(data)
with open("7.txt","w") as f1:
    data=f1.write("new data added")
    print()
import os
os.remove("7.txt")"""
"""with open("7.txt","w") as p:
    data=p.write("Hi everyone \nwe are learning file i/o \nusing java.\ni lile programmming in java")
    print(data)"""
"""with open("7.txt","r") as f:
    data=f.read()
newdata=data.replace("java","python")
print(newdata)
with open("7.txt","w") as f:
    f.write(newdata)"""
word="learning"
with open("7.txt","r")as p:
    data=p.read()
    if(data.find(word) != -1):
        print("learning is found")
    else:
        print("learning is not found")


