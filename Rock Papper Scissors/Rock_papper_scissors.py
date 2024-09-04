'''
Rock = 1
Papper = 0
Scissor = -1

'''
import random
n= random.randint(-1,1)

Computer = n
Your_choice = input("Enter Your Move (r,p,s) : ")
Dict = {"r":1, "p":0, "s":-1}
You =  Dict[Your_choice]

if(Computer == You):
    print("Draw!")
else:
    if(Computer==-1 and You == 1):
        print("You Won!")
    elif(Computer==-1 and You == 0):
        print("You Lost!")

    elif(Computer==1 and You == 0):
        print("You Won!")
    elif(Computer==1 and You == -1):
        print("You Lost!")


    elif(Computer==0 and You == -1):
        print("You Won!")
    elif(Computer==0 and You == 1):
        print("You Lost!")

    else:
        print("Something Went Wrong...")


ReverseDict = {1:"Rock", 0:"Paper", -1:"Scissor"}
print(f"Your Choice : {ReverseDict[You]}\nComputer Choice : {ReverseDict[Computer]}")

