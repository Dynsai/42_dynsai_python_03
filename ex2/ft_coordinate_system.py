import math
# import math, math.sqrt(), input(), round(), print()


def input_function() -> tuple:
    coordinates: list = []
    while True:
        try:
            coordinates.append(float(input("= Introduce X coordinate: ")))
            print(f"X: {coordinates[0]}")
            break
        except ValueError:
            print("Invalid X coordinate. Please introduce a numerical value.")
    while True:
        try:
            coordinates.append(float(input("= Introduce Y coordinate: ")))
            print(f"Y: {coordinates[1]}")
            break
        except ValueError:
            print("Invalid Y coordinate. Please introduce a numerical value.")
    while True:
        try:
            coordinates.append(float(input("= Introduce Z coordinate: ")))
            print(f"Z: {coordinates[2]}")
            break
        except ValueError:
            print("Invalid Z coordinate. Please introduce a numerical value.")
    return tuple(coordinates)


def coordinate_system() -> None:
    coordinates: tuple[float, float, float] = input_function()
    label: list = ["X", "Y", "Z"]
    print(f"{coordinates}")
    i: int = 0
    for coord in coordinates:
        print(f"{label[i]}: {coord}")
        i += 1
    print("Let's compare your coordinates with the center (0.0, 0.0, 0.0)")
    distance_center: float
    distance_center = math.sqrt((coordinates[0] - 0)**2
                                + (coordinates[1] - 0)**2
                                + (coordinates[2] - 0)**2)
    print(f"Distante from the center is: {round(distance_center, 2)}")
    print("Let's compare the first set of cordinates with another set")
    new_coordinates: tuple[float, float, float] = input_function()
    distance_coords: float
    distance_coords = math.sqrt((new_coordinates[0] - coordinates[0])**2
                                + (new_coordinates[1] - coordinates[1])**2
                                + (new_coordinates[2] - coordinates[2])**2)
    print(f"Distance between coordinates is: {round(distance_coords, 2)}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    coordinate_system()
    print("End of program")
