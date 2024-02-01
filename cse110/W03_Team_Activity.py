#Rectangle

'''Rectangle_Length = int(input("What is the rectangle length?: "))
Rectangle_Width = int(input("What is the rectangle width?: "))
Rectangle_Area = Rectangle_Length*Rectangle_Width
print(f"The rectangle area is: {Rectangle_Area}")

#Square
Square_Length = int(input("What is the square length?:"))
Square_Area = Square_Length**2
print(f"The area of the square is: {Square_Area}")

#Circle
from math import pi
Circle_Radius = int(input("What is the raduis of the circle?: "))
Circle_Area = pi*Circle_Radius**2
print(f"The area of the circle is: {Circle_Area}")'''

#Stretch challenge
#from math import pi
#print(pi)
from math import pi
Length_Value = int(input("Enter the length value please: "))
Square_Area = Length_Value**2
Circle_Area = pi*Length_Value
Volume_Cube = Length_Value**3
Sphere_Volume = 4/3*pi*Length_Value**3
print(f"The area of the square is: {Square_Area}")
print(f"The area of the circle is: {Circle_Area}")
print(f"The Volume cube is: {Volume_Cube}")
print(f"The sphere volume is: {Sphere_Volume}")