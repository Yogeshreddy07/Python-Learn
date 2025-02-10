#SETS
#s={} for empty Dictionary
e=set() # empty set

s={1,1,3,2,3,23,55,6}
s1={1,1,2,3,4,533,3}
print(s) #{1, 2, 3, 23, 6, 55} no repetation in sets

s.add(566)
print(s)#{1, 2, 3, 23, 6, 55, 566}

print(len(s)) #7

s.remove(6) 
print(s) #{1, 2, 3, 23, 55, 566}

s.pop()
print(s) #it remove a random element

s.clear()
print(s)#set() empty set

#union it takes both the values of set and writen theall value except the repeted one.
print(s.union(s1))

#intersect it print oly the common values
print(s.intersection(s1))