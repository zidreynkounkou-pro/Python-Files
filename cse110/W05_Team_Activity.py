grade = float(input("What's your percentage? "))
if grade >= 90:
    grade_letter = "A"
elif grade >= 80:
    grade_letter = "B"
elif grade >= 70:
    grade_letter = "C" 
elif grade >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"
    
# Stretch challenge 1
sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
    
# Stretch challenge 2 
if grade >= 93:
    sign = ""
    
# Stretch challenge 3
if grade_letter == "F":
    sign = ""
    
print(f"Your letter grade is {grade_letter}{sign}")
if grade >= 70:
    print(" You passed the course. Congratulations!")
else:
    print("You failled the course. We encourage you to apply for the next term!")
    
    

    














