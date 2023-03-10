import random

print("Welcome to the Number Guessing Game\nI am thinking about a number between 1 to 100")
question = input("Choose your difficulty level, hard or easy :")

random = random.randint(0, 100)
lives_easy = 10
lives_hard = 5

end_game = False
while not end_game:
    if question == "easy":
        print(f"You have {lives_easy} attempts remaining.")
        guess = int(input("Make a Guess:"))
        if guess != random and guess > random:
            print("Too high")
            lives_easy -= 1
            if lives_easy == 0:
                print("You are out of lives")
                end_game = True
        elif guess != random and guess < random:
            print("Too low")
            lives_easy -= 1
            if lives_easy == 0:
                print("You are out of lives")
                end_game = True
        else:
            print("That's the correct number")
            end_game = True
            
    elif question == "hard":
        print(f"You have {lives_hard} attempts remaining.")
        guess = int(input("Make a Guess:"))
        if guess != random and guess > random:
            print("Too high")
            lives_hard -= 1
            if lives_hard == 0:
                print("You are out of lives")
                end_game = True
        elif guess != random and guess < random:
            print("Too low")
            lives_hard -= 1
            if lives_hard == 0:
                print("You are out of lives")
                end_game = True
        else:
            print("That's the correct number")
            end_game = True
