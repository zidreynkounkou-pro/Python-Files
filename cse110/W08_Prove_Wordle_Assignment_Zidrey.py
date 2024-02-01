user_name = input("Enter your full name here please: ").title()
print()
print("Welcome to the word guessing game dear",user_name + "!")
print()

import random

# List of words
book = ["mosiah","moroni","2nephi","ether","3nephi","helaman","1nephi","jacob","mormon","4nephi","alma","enos","jarom","words of mormon"]

# Variables
secret_word = random.choice(book)
guess = ""
count_guesses = 0

while True:
    hint = ["_"]*len(secret_word)
    
    # The initial hint
    print("Your hint is: "," ".join(hint))
    break

    # Starting with the Loop

while guess is not secret_word:

    guess = input("What is your guess? ").lower()

    if len(secret_word) is not len(guess):
        print("Sorry, the guess must have the same number of letters as the secret word")
        count_guesses += 1 # or count guesses = count_guesses + 1
        continue

    count_guesses += 1

        # Checking if the guess is correct
    if guess == secret_word:
        print("Congratulations! You guessed it.")

        if count_guesses > 1:
            print(f"It took you {count_guesses} guesses.\n" + "Thank you for playing!" + "\nGoodbye " +  user_name + "!")
            break
        else:
            print(f"It took you {count_guesses} guess.\n" + "Thank you for playing!" + "\nGoodbye " + user_name + "!")
            break
            
# Checking the guess in the secret word, then providing a hint

    hint_s = []
    for j in range(len(secret_word)):

        if guess[j] == secret_word[j]:
             
            hint_s.append(secret_word[j].upper())
             
        elif guess[j] in secret_word:
            
            hint_s.append(guess[j].lower())
        else:
            hint_s.append("_")

    print(f"Your hint is: " + " ".join(hint_s))






