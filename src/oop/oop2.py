# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, name, num_wheels=4):
        self.name = name
        self.num_wheels = num_wheels

    def drive(self):
        # Tico's Tesla Example
        # return f"Vehicle Name: {self.name}, Number of Wheels: {self.num_wheels}"
        return "vroooom"

x = GroundVehicle("Tesla", 6)

print(x.drive())


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, name, num_wheels=2):
        super().__init__(name, num_wheels)
        self.num_wheels = num_wheels
        self.new_sound = "BRAAAP!!"
    def drive(self):
        # Tico's Ducati Example
        # return f"Motorcycle Name: {self.name}, Number of Wheels: {self.num_wheels}"
        return self.new_sound

y = Motorcycle("Ducati", 4)

print(y.drive())

# vehicles = [
#     GroundVehicle(),
#     GroundVehicle(),
#     Motorcycle(),
#     GroundVehicle(),
#     Motorcycle(),
# ]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
