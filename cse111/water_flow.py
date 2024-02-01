# exceeding requirements
acceleration_from_Earths_gravity = 9.80665 # meter / second^2
density_of_water = 998.2 # kilogram / meter^3
dynamic_viscosity_water = 0.0010016 # pascal seconds

def water_column_height(tower_height, tank_height):
    """
    this is the water column height function that calculates and returns the height of a column of water from a tower height and a tank wall height.

    parameters:
    tower_height: the height of the tower
    tank_height: the height of the tank

    """
    h = tower_height + ((3 * tank_height) / 4)
    return h

def pressure_gain_from_water_height(height):
    """this is the pressure gain from water height function that calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.

    parameter:
    height: the height of the water column in meters.""" 

    p = (density_of_water * acceleration_from_Earths_gravity * height) / 1000
    return p

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """This is the pressure loss from pipe function that calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through and returns it.

    parameters:
    pipe_diameter,
        pipe_length, friction_factor and fluid_velocity."""

    
    p = (-density_of_water * pipe_length * friction_factor * (fluid_velocity ** 2)) / (2000 *  pipe_diameter)

    return p 

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    "calculate the pressure loss from fittings function that calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline and returns it."

    "parameter: fluid_velocity and quantity_fittings"

    p = (-0.04 * density_of_water * quantity_fittings * (fluid_velocity ** 2)) / 2000

    return p

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    this is the reynolds number function that calculates and returns the Reynolds number for a pipe with water flowing through it and returns it.

    parameters:
    hydraulic_diameter and fluid_velocity
    
    """
    r = (density_of_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_water 
    return r

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """the pressure loss from pipe reduction that calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter and returns it.

    parameters:
    large_diameter, smaller_diameter, fluid_velocity and reynolds_number"""

    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4 ) -1)

    p = -k * density_of_water * (fluid_velocity ** 2) / 2000

    return p

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()