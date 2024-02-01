print("Welcome to the word guessing game!")
print()

secret_word = "harmony"
guess_word = ""
count = 0
hint = ("____")
import random 

while guess_word.lower() != secret_word:
    
    for i in secret_word:
        if i in guess_word:
        
            print(f"Your hint is",i.upper())
    
            print(i)
        else:
            print("_")
        for j in secret_word:
            if guess_word in j:
                print(guess_word.lower())
        #elif i != guess_word:
        #    print(f"Your hint is",guess_word)
    



            #print(i.lower())
        
        
            
            
            
            
        #if guess_word == secret_word[0] or guess_word == secret_word[1] or guess_word == secret_word[2] or guess_word == secret_word[3] or guess_word == secret_word[4]:
            

                  
    guess_word = input("What is your guess? ")
    for i in secret_word:
        if i == guess_word.lower:
            print(i.upper())
        
    if guess_word == secret_word:
        print("Congratulations! You guessed it!")
        count += 1
    else:
        print("Your guess was not correct.")
        count += 1
if count > 1:
    print(f"It took you {count} guesses.")
else:
    print(f"It took you {count} guess.")