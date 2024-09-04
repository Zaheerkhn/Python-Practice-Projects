import random

rand_num = random.randint(1,100)

heading = "Welcome to Number Guessing Game"
print(heading.center(100))

win = False
cnt_steps = 1

start = "Do You Want to Play the game ?"
print(start)
ans = input("Enter Yes or No : ")

dec_dict = {"yes": 1 , "no": 0}

your_ans = dec_dict[ans]
print("\n")
if(your_ans == 1):

    while(win != True):
        
        guess = int(input("Guess the Number : "))

        if(guess > rand_num):
            print("The number you have guessed is higher than the actual Number, Guess Again!")
            cnt_steps = cnt_steps + 1

        elif(guess < rand_num):
            print("The number you have guessed is Lesser than the actual Number, Guess Again!")
            cnt_steps = cnt_steps + 1

        else:
            print("The Number you have guessed is Right!\nYou WIN!")
            win = True

    print(f"The Number of steps you used in this round is {cnt_steps} and the Number you have guessed is {rand_num}.")

else:
    print("No problem you can play anytime you want.")