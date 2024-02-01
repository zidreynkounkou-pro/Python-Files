import random
repeat = "yes"
while repeat == "yes":
    
    number = random.randint (1, 100)
    guess = -1
    count = 0
    while guess != number:
        guess = int (input ("What is your guess? "))
        if guess < number:
            print ("Higher")
            count += 1
        elif guess > number:
            print ("Lower")
            count += 1
        else:
            print ("You guessed it!")
            count += 1
    print (f"You made {count} guesses.")
    repeat = input ("Would you like to play again (yes/no)? ")
print ("Thank you for playing.")
