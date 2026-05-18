import math
# import math, math.sqrt(), input(), round(), print()

def input_function() -> tuple:
    coordinates: list = []
    while True:
        try:
            coordinates.append(float(input("= Introduce X coordinate: ")))
            print(f"X: {coordinates[0]}")
            break
        except ValueError as error:
            print("Invalid X coordinate. Please introduce a numerical value.")
    while True:
        try:
            coordinates.append(float(input("= Introduce Y coordinate: ")))
            print(f"Y: {coordinates[1]}")
            break
        except ValueError as error:
            print("Invalid Y coordinate. Please introduce a numerical value.")
    while True:
        try:
            coordinates.append(float(input("= Introduce Z coordinate: ")))
            print(f"Z: {coordinates[2]}")
            break
        except ValueError as error:
            print("Invalid Z coordinate. Please introduce a numerical value.")
    return tuple(coordinates)


def coordinate_system() -> None:
    coordinates: tuple = input_function()
    label: list = ["X", "Y", "Z"]
    print(f"{coordinates}")
    i: int = 0
    for coord in coordinates:
        print(f"{label[i]}: {coord}")
        i += 1

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    coordinate_system()
    print("End of program")


# First, write a function get_player_pos() that:
# • Asks the user for the new player coordinates in the format x,y,z
# • Handles improper inputs
# • Retries until a valid set of coordinates is provided
# • Returns a tuple containing the player’s current 3D coordinates
# Then your code will:
# • Get a first set of coordinates
# • Display the tuple then display each coordinate separately
# • Calculate the distance to the 3D center (0, 0, 0) (see below)
# • Get a new set of coordinates
# • Calculate the distance between the second and the first sets of coordinates

# Distance Formula: To calculate the distance between two 3D points, we use the Eu-
# clidean distance formula
# √
# (x2 − x1)2 + (y2 − y1)2 + (z2 − z1)2 .
# For points (x1, y1, z1) and (x2, y2, z2), the distance is math.sqrt((x2-x1)**2 +
# (y2-y1)**2 + (z2-z1)**2). This is just the 3D extension of the Pythagorean theorem!

# $> python3 ft_coordinate_system.py
# === Game Coordinate System ===
# Get a first set of coordinates
# Enter new coordinates as floats in format 'x,y,z': hello world
# Invalid syntax
# Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0
# Got a first tuple: (1.0, 2.5, 3.0)
# It includes: X=1.0, Y=2.5, Z=3.0
# Distance to center: 4.0311
# Get a second set of coordinates
# Enter new coordinates as floats in format 'x,y,z': 4,abc,5
# Error on parameter 'abc': could not convert string to float: 'abc'
# Enter new coordinates as floats in format 'x,y,z': 4,5,6
# Distance between the 2 sets of coordinates: 4.9244