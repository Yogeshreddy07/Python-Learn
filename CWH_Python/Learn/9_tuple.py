#tuple are immutable

a = () # empty tuple 
a = (1,) # tuple with only one element needs a comma 
a1 = (1,7,2,2) # tuple with more than one element 

print(type(a)) #<class 'tuple'>

#funtion in string
a11=a1.count(7) #counts the accurence of the value inside the count function
print(a11) #1

#index()will return the index of first occurrence of 1 in a1
b=a1.index(1)
print(b) #0

print(len(a1)) #print the length of the tuple ->(4)







