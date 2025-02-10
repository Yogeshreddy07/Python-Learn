#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
#type 1 update for key thats present
dic={"yogesh":"",
     "reddy":"",
     "syogesh":""
     }
i=input("enter your name:")
l=input("enter the lang:")
dic[i]=l
print(dic)

print("\n")

#type 2 both input:
dic1={}
name=input("Enter the name:")
lang=input("enter the lang:")
dic1.update({name:lang})

name=input("Enter the name:")
lang=input("enter the lang:")
dic1.update({name:lang})

name=input("Enter the name:")
lang=input("enter the lang:")
dic1.update({name:lang})

name=input("Enter the name:")
lang=input("enter the lang:")
dic1.update({name:lang})
print(dic1)
"""{'yogesh': 'telugu', 'yogeshreddy': 'telugu', 'reddy': 'english', 'reddy1': 'telugu'}"""