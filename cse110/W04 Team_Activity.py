import math

# Variables 
print("Welcome to the velocity calculator. Please enter the following: ")
mass = float(input(("Mass (in kg): ")))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter)"))
time = float (input("Time (in seconds): "))
fluid_density = float (input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sect_area = float (input("Cross sectional area (in m^2): "))
drag_constant = float (input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# The inner value c = (1/2) * A * P * C. With A: cross_sect_area, P: fluid_density, C: drag_constant

c = (1/2) * cross_sect_area * fluid_density * drag_constant
print(f"The inner value of c is: {c:.3f}")
v_at_t = math.sqrt(mass * gravity / c) * (1 - math.exp((- math.sqrt(mass * gravity * c) / mass * time)))
print(f"The velocity at {time} seconds is: {v_at_t: .3f} m/s")
