"""1="snake"
2="water"
3="gun"
"""
import random #used to genrate the random value
computer= random.choice([1,2,3])
inuser=input("Enter (s for Snake, w for Water, g for Gun):").lower()
choice={
    "s":1,
    "w":2,
    "g":3
}
i2=computer
i1=choice[inuser]
rechoice={
    1:"Snake",
    2:"water",
    3:"gun"
}
print(f"Player chose: {rechoice[i1]} \nComputer chose: {rechoice[i2]}")
if(i1 == i2):
    print("It's a Draw! Both chose the same.")
else:
    if(i1==1 and i2==2):
        print("Snake drinks the water hence you wins..")
    elif(i1==2 and i2==3):
        print(f"The gun will drown in water, hence you wins")
    elif(i1==3 and i2==1):
        print("Gun will kill the snake and hence you wins")
    elif(i2==1 and i1==2):
        print("Snake drinks the water hence player computer wins")
    elif(i2==2 and i1==3):
        print("The gun will drown in water, hence computer wins")
    elif(i2==3 and i1==1):
        print("Gun will kill the snake and hence computer wins")
    else:
        print("Invalid input! Please enter 's', 'w', or 'g'.")

    
