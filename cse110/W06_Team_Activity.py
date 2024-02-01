
can_ride = False

age_rider_1 = int(input("What is the age of the first rider? "))
height_rider_1 = float(input("What is the height of the first rider? "))
rider_2 = input("Is there a second rider (yes/no)? ")
rider_yes = "yes"

if rider_2.lower() == rider_yes:
    age_rider_2 = int(input("What is the age of the second rider? "))
    height_rider_2 = float(input("What is the height of the second rider? "))
else:
    if age_rider_1 >= 18 and height_rider_1 >= 62:
        can_ride = True 
    else:
        can_ride = False
if height_rider_1 < 36 and height_rider_2 < 36:
    can_ride = False
elif height_rider_1 < 36:
    can_ride = False
else:
    if rider_2 == rider_yes:
        if age_rider_1 >= 18 or age_rider_2 >= 18:
            can_ride = True
        else:
            can_ride = False
if rider_2 == rider_yes:
    if height_rider_2 < 36:
        can_ride = False  
if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride!")


"""No one under 36 inches may ever ride, either by themselves or with another rider.

Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

If there are two riders and one of them is at least 18 years old, they may ride together.

Assignment
Implement the ride requirements defined above. Your program should prompt for the riders' ages and heights, and then display a message indicating whether they can ride or not.

CORE REQUIREMENTS
Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.

Handle the case of a single rider.

Finish implementing the basic rules."""





