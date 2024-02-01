print("Please enter the following information:")
print()

First_Name = input("First name: ").capitalize()
Last_Name = input("Last name : ").upper()
Email_Address = input("Email address: ").lower()
Phone_Number = input("Phone number: ")
Job_Title = input("Job title: ").title()
ID_Number = input("ID: ")


# Stretch Challenge
Hair_Color = input("Hair: ").capitalize()
Eyes_Color = input("Eyes: ").capitalize()
Month = input("Month of the begining: ").capitalize()
Training_or_not = input("Is there any training completed?: ").capitalize()
print()

print("The ID Card is: ")
print("-------------------------------------------------------------------------------------------------")
print(f"{Last_Name}, {First_Name}")
print(Job_Title)
print(f"ID: {ID_Number}")
print()

#Stretch Challenge
print(Email_Address)
print(Phone_Number)
print()
print(f"Hair: {Hair_Color:20} Eyes: {Eyes_Color}")
print(f"Month: {Month:19} Training: {Training_or_not}")


print("-------------------------------------------------------------------------------------------------")