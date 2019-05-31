# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # Base Class
    pass

class GroundVehicle(Vehicle):
    # Sub Class #1 of Vehicle
    pass

class Car(GroundVehicle):
    # Sub Class A of GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    # Sub Class B of GroundVehicle
    pass

class FlightVehicle(Vehicle):
    # Sub Class #2 of Vehicle
    pass

class Airplane(FlightVehicle):
    # Sub Class A of FlightVehicle
    pass

class Starship(FlightVehicle):
    # Sub Class B of FlightVehicle
    pass


