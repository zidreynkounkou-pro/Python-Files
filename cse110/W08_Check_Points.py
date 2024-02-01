"""colors = ["red", "blue", "green", "yellow"]
for i in colors:
    print(i)"""
#numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#for i in range(2, 21, 2):
#    print(i)


secret_word = "commitment"

fav_letter = input("What is your favorite letter? ")

for lett in secret_word:
    if lett.lower() == fav_letter.lower():
        print(lett.upper(), end = "")
    else:
        print(lett.lower(), end = "")                                                

print()

for lett in secret_word:
    if lett.lower() == fav_letter.lower():
        print("====", end = "")
    else:
        print(lett.lower(), end = "")





        





