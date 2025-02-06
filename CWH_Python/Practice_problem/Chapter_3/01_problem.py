#Write a python program to display a user entered name followed by Good Afternoon using input () function. 
input=str(input("Enter your name:"))

#type 1
print("Good Afternoon,",input,"!".strip()) #(Good Afternoon, yogesh !)

#type 2
print(f"Good Afternoon,{input}!") #Good Afternoon,yogesh!