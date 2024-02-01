"""mport random 

guess_number = ""

number = random.randint(1,100)

while guess_number is not number:
    
    guess_number = int(input("What's your guess? "))
    if guess_number < number:
        print("Higher!")
    elif guess_number > number:
        print("Lower!")
    else:
        print("You guessed it!")"""
"""List = ["Relga", "Zidrey", "Nkounkou"]
print (" ".join(List))
print(List)"""

word = "commitment"
l = input("EN here ")
for letter in word:
    if letter.lower() == l.lower():
        print(letter.upper(), end = "")
    else:
        print(letter.lower(), end = "")





