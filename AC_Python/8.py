class Student:
    #def __init__ (): #default constructor
    #    pass
    collage="Alliance University" #class  attribute used to call in every constructor
    def __init__(self,fname,mark):
        print("adding the new student in the data base") #parametarised constructor
        self.name = fname
        self.mark =mark
s1=Student("yogesh reddy",9)
print(s1.name,s1.mark)
print(s1.collage)
s2=Student("pavithra",10)
print(s2.name,s2.mark)

  
"""class cars:
    name="audi"
    colour="black"
s1=cars()
print(s1.name)
print(s1.colour)"""
