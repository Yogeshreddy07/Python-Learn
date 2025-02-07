#Dictionary is a collection of keys-value pairs
dic={
    "yogesh":87,
    "mnj":87,
    "rfed":84,
    "ffdd":54
}

print(type(dic)) #<class 'dict'>

print(dic) #{'yogesh': 87, 'mnj': 87, 'rfed': 84, 'ffdd': 54}
print(dic.items()) #dict_items([('yogesh', 87), ('mnj', 87), ('rfed', 84), ('ffdd', 54)])
print(dic.keys())  #dict_keys(['yogesh', 'mnj', 'rfed', 'ffdd'])
print(dic.values()) #dict_values([87, 87, 84, 54])
#print(dic[0]) #dosent print whats there in that index
print(dic["yogesh"])

dic["yogesh"]=99
print(dic) #{'yogesh': 99, 'mnj': 87, 'rfed': 84, 'ffdd': 54}

dic.update( {"yogesh": 100 })
print(dic) #{'yogesh': 100, 'mnj': 87, 'rfed': 84, 'ffdd': 54}

dic.update( {"yogesh": 100 ,"reddy":93}) #the key which is not thare that will be added at end 
print(dic) #{'yogesh': 100, 'mnj': 87, 'rfed': 84, 'ffdd': 54, 'reddy': 93}

dic.get("yo")
print(dic) #None
#print(dic["ha"]) #returns error
