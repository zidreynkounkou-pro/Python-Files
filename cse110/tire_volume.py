from datetime import datetime
from math import pi
# asking the user to enter the width, aspect ratio and diameter of the tire
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
# space
print()
# compute the volume of space inside the tire
w = width
a = ratio
d = diameter
i = pi * (w ** 2) * a * (a * w + (2540 * d))
v = i / 10000000000
# display the result
print(f"The approximate volume is {v: .2f} liters")
# find current date and time 
current_date = datetime.now()

# exceed the requirements
# ask the user they want to buy tires with the dimensions they entered
user = input("Do you want to buy tires with the dimensions you entered? (Yes/No): ")
# check if the user answered yes
if user.lower() == "yes":
    # ask the user's phone number
    phone_number = input("Enter your phone number, please: ")
    # open a file volumes.txt in append mode
    with open("volumes.txt", "at") as volume_file:
        # append the current date and time, width, ratio, diameter, volume of the tire
        # and the user's phone number to the volumes.txt file
        volume_file.write(f"{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {v: .2f}, {phone_number}\n")
else: # if the user answered no
    with open("volumes.txt", "at") as volume_file:
        # append the current date, width, ratio, diameter and the volume of the tire
        # # to the volumes.txt file
        volume_file.write(f"{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {v: .2f}\n")
