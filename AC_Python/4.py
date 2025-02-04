#dictionery
"""
dict1={"name":"yogesh",
       "cgpa":9.1,
       "age":18,
       "is_adult " : True
       ,"sub" :["py","c++"]}

print(type(dict1))
print(dict1)
print("the name is", dict1["name"])
dict1["name"]="Yogesh Reddy"
print("the changed name is",dict1["name"])
null_duct={} #its a null dictonery
null_duct["name"]="yogesh"
print(null_duct)
""" 
student={
    "name":"yogesh",
    "sub":{"python":99,
           "c++":70
           }
}
print(student) 
print(student.keys())      #used to display the keys
print(student.values())    #used to display thwe values
print(list(student))       #used to convert int to the list
print(student.items())     #used to display the both the key and value
print(student.get('name')) #used to get the value taking the key as input

student.update({"cgpa" : 8.7})
print(student)

set1={"py","java","c++","python","javascript"}
set2={"java","c"}
set1.union(set2)
print(set1)