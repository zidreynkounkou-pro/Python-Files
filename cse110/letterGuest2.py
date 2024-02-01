#import random

# Define the secret word
secret_word = "mosiah"

# Convert the secret word to lowercase
secret_word = secret_word.lower()

# Create a list of underscores with the same length as the secret word
underscore_list = ["_"] * len(secret_word)

# Print the initial hint
print("Welcome to the word guessing game!\n")
print("Your hint is: " + " ".join(underscore_list))

# Initialize the number of guesses to 0
num_guesses = 0

# Start the game loop
while True:

    # Ask the user for a guess
    guess = input("\nWhat is your guess? ").lower()

    # Check if the guess has the same number of letters as the secret word
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        num_guesses += 1
        continue

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == secret_word:
        print("\nCongratulations! You guessed it!")
        print("It took you " + str(num_guesses) + " guesses.")
        break

    # If the guess is incorrect, provide a hint
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(secret_word[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())
        else:
            hint.append("_")
    print("Your hint is: " + " ".join(hint))