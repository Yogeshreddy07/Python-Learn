#string function and escape seqence

name="yogesh"
#finds the length of the string
print(len(name)) #finds the length name (6)

#finds the startswith which letter 
print(name.startswith("y")) #True

#finds the endswith which letter 
print(name.endswith("g")) #False

#it counts the total number of occurrences of any character
count = name.count("r") 
print(count) # (0)

#it cap First character of a given string
cap=name.capitalize()
print(cap) #Yogesh

#string.find(word) – This function friends a word and returns the index of first occurrence of that word in the string.
find=name.find("o")
print(find)

#string.replace (old word, new word ) – This function replace the old word with new word in the entire string.
replaced_string = name.replace("yogesh", "reddy") 
print(replaced_string)  # Output: "reddy"

# .strip() reduce the space
print(" yogesh ".strip() ," reddy ".strip())

#escape sequence
#\n-> next line
a="yogesh is a good boy \nbut not a bad boy\n"
print(a)

#\t gives a tab space
a="yogesh is a good boy \nbut not a \t bad boy\n"
print(a)

#\" "\ or \''\ used to insert "" or'' in the line when "" or'' already in use
a="yogesh is a good boy \nbut not a \"bad\" boy "
print(a)
