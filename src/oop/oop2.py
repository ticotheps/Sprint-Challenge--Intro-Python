# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, name, num_wheels):
        self.name = name
        self.num_wheels = num_wheels

    def Drive(self):
        return f"Vehicle Name: {self.name}, Number of Wheels: {self.num_wheels}"

x = GroundVehicle("Tesla", 4)

print(x.Drive())


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

# vehicles = [
#     GroundVehicle(),
#     GroundVehicle(),
#     Motorcycle(),
#     GroundVehicle(),
#     Motorcycle(),
# ]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
