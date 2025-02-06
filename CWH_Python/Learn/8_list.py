#list ->are mutable
friends=["Apple","orange",5,65.55,False,"yogi"]
num=[2,2,4,67,3,1,0]
num1=[2,2,4,67,3,1,0]
print(friends) #['Apple', 'orange', 5, 65.55, False, 'yogi']
#list SLICING using index
print(friends[0]) #['Apple']
print(friends[1:4]) #['orange', 5, 65.55]

friends[0] = "reddy"
print(friends) #['reddy', 'orange', 5, 65.55, False, 'yogi']

#methods
#sort function used to arrange in adc order
num.sort()
print(num) #[0, 1, 2, 2, 3, 4, 67]

#sort function used to arrange in dec order
num.sort(reverse=True)
print(num)  #[67, 4, 3, 2, 2, 1, 0]
#type 2
num1.reverse()
print(num)

#This will add 8 at 3 index 
num1.insert(3,8)
print(num1)

#Will delete element at index 2 and return its value
num1.pop(2)
print(num1)

num1.remove(1)
print(num1)                                 #[0, 8, 67, 4, 2, 2]

#adds at the end of the list
friends.append("shiva")
print(friends)                              #['reddy', 'orange', 5, 65.55, False, 'yogi', 'shiva']

