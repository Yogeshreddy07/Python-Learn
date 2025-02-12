print("Welcome to the game!! ,Enter ( Snake or Water or Gun) as a choice")
i1=input("Enter the input player 1:").lower()
i2=input("Enter the input player 2:").lower()
print(f"The player 1 as entered : {i1} \nThe player 2 as entered : {i2}")
if(i1 ==i2):
    print("It's a Draw! Both chose the same.")
elif(i1 != i2):
    if(i1=="snake" and i2=="water"):
        print("Snake drinks the water hence player 1 wins..")
    elif(i1=="water" and i2=="gun"):
        print(f"The gun will drown in water, hence player 1 wins")
    elif(i1=="gun" and i2=="snake"):
        print("Gun will kill the snake and hence player 1 wins")
    elif(i2=="snake" and i1=="water"):
        print("Snake drinks the water hence player 2 wins")
    elif(i2=="water" and i1=="gun"):
        print("The gun will drown in water, hence player 2 wins")
    elif(i2=="gun" and i1=="snake"):
        print("Gun will kill the snake and hence player 2 wins")
    else:
        print("Invalid input! Please enter 'snake', 'water', or 'gun'.")