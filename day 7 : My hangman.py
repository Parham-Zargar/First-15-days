import random

word_list = ["aadrdvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
display = []
for i in range(len(chosen_word)):
    display += "_"

while not display == chosen_word:
    guess = input(" Guess a letter : ")
    if guess in display:
        lives -= 1
        print(f"You've already guessed the  (( {guess} ))\nYou lost a live \nYour remaining lives is {lives}")

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed ( {guess} )\nthat's not in the word. \nYou lose a life.")
        print(f"You're remained lives is {lives}")
    if lives == 0:
        print("You've lost")
        break
    if "_" not in display:
        print(f"{' '.join(display)}")
        print("You Win")
        break
    print(display)
