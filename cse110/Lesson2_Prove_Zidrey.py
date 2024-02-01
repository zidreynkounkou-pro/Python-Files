User_full_name = input("Enter your full name here please: ").title()
print(f"Hi dear {User_full_name}, we welcome you here! Enjoy your game!")

print('\n')
print("Please enter the following:")

# Space
print('\n')

# Variables
Adjective = input("adjective: ")
Animal = input("animal: ")
Verb1 = input("verb: ")
Exclamation = input("exclamation: ").capitalize()
Verb2 = input("verb: ")
Verb3 = input("verb: ")

# Space 
print('\n')

# Story
print("Your story is: ")
print('\n')
print(f"The other day, I was really in trouble. It all started when I saw a very {Adjective} {Animal} {Verb1} down the hallway. {Exclamation}!\
 I yelled. But all I could do was to {Verb2} over and over. Miraculously,  that caused it to stop, but not before it tried to {Verb3} right in\
 front of my family.")
print('\n')

# My adds
Enjoy_or_not = input("Have you enjoyed the game? yes or no? (write your response in lowercase please!)")
if Enjoy_or_not == "yes":
    print("We are happy that you have enjoyed the game!")
else:
    print("We are sorry that you have not enjoyed the game!")