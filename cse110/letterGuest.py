from ctypes.wintypes import PINT

word = 'commitment'
tries = 0
display = '_'*len(word)

print()
print('Welcome to the word guessing game!')
print()

game_over = False
while not game_over:
    print(f"Your hint is: {display}")
    
    word_guessed = input("What is your guess? ")
    if len(word_guessed) != 1:
        print('Please enter a single character.')
        continue
    
    if word_guessed in word:
        tries += 1
        i = 0
        while i < len(word):
            if word[i] == word_guessed:
                display = display[:i] + word_guessed + display[i + 1:]
            i += 1
        
        print('Correct!')
                
    else:
        print('Sorry, wrong guess.')
        tries += 1

    if word == display:
        print(f"You win! The word was {word}")
        print(f"It took you a total of {tries} guesses!!")
        game_over = True
        
    if tries == len(word):
        print('Sorry, you are out of attempts.')
        game_over = True