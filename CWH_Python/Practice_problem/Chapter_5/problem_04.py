"""What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? """ 
s = set() 
s.add(20)  
s.add(20.0) 
s.add('20') 
print(s)      #{'20', 20} so 20,20.0 will same will not diff as the int and the float
print(len(s)) # length of s after these operations? ->> 2

s1 = {} 
#What is the type of 's'? 
print(type(s1)) #dict -> <class 'dict'>