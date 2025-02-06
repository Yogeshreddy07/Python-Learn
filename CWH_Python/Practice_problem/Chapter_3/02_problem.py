"""Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''  """
inputname=input("Enter the name:")
inputdate=input("Enter the date:")
#Type 1
print("Dear",inputname,",\nyou are selected!\n",inputdate,"\n'''") #type one

#Type 2
print(f"Dear<|{inputname}|>,\nyou are selected!\n<|{inputdate}|>\n'''")
