#list
"""yogesh=[98,88,99,88,99]
print(yogesh) #for printing the value in side thethe list
print(yogesh[1],yogesh[0]) #acessing the index value using index
print(yogesh[0:5]) #Slicing 
print(yogesh[:4])  #Slicing for starting from 0 upto 3(index) place
print(yogesh[1:])  #Slicing for starting from 1 upto 4(index) place not include the 0 index
"""
list=[85,94,76,63,67] #int
"""list1=["n","a","f","r"] #strings
list.append(99)
print(list.append(99)) # prints None but again add the 99 means it dose its work but prints none
print("Adds the element 99",list) 
list.sort()
print("sorted the element in ascending order",list)
list.sort(reverse=True)
print("sorted the element in decednding order",list)
list1.sort() 
print("sorted the element in ascending order for str",list1)
list.reverse()
print("reverse of the list will be printed",list)
list.insert(1,2) #instert the value based on the index ->>list.insert( index, data(str,int, float ,etc))
print(list)
list.remove(85)
print(list)# remove 85
list.pop(1)
print(list)# removes the number based on the index

if 85 in list:
    print("yes 85 there in the list")
#input in list
l=str(input("Enter the elements")).split()
print(l)

l1=[]
l1.append(input("enter the element 1:"))
l1.append(input("enter the element 2:"))
l1.append(input("enter the element 3:"))
print(l1)
print(type(l1))

l1=[1,2,3,1]
l=l1.copy()
l.reverse()
if (l == l1):
    print("its a palendrome")
else:
    print("not a palendrome")

tup = ("c","d","a","a","b","b","a")
print(tup.count("a"))
"""
tup = ["c","d","a","a","b","b","a"]
tup.sort()
print(tup)
