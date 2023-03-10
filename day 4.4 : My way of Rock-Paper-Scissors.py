import random

user_choice = input("What do you choose ? Rock, Paper , or Scissors :  ")

game = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(game)

if user_choice == "Rock" and computer_choice == "Rock":
    print("You've chosen Rock \nComputer chose Rock. That's tie")
elif user_choice == "Rock" and computer_choice == "Paper":
    print("You've chosen Rock \nComputer chose paper, You lose")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You've chosen Rock \nComputer chose scissors, You Win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You've chosen Paper\nComputer chose rock, you win")
elif user_choice == "Paper" and computer_choice == "Paper":
    print("You've chosen Paper\nComputer chose paper. That's tie")
elif user_choice == "Paper" and computer_choice == "Scissors":
    print("You've chosen Paper\nComputer chose scissors, you lose")
elif user_choice == "Scissors" and computer_choice == "Rock":
    print("You've chosen Scissors\nComputer chose rock, you lose")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You've chosen Scissors\nComputer chose paper. You win")
elif user_choice == "Scissors" and computer_choice == "Scissors":
    print("You've chosen Scissors\nComputer chose scissors, That's tie")

else:
    print("You've chosen a wrong name.")
