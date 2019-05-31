# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

    def getNameOnly(self):
        return self.name

    def getAgeOnly(self):
        return self.age

    def getNameAndAge(self):
        return (self.name, str(self.age))
    
    def getNameAndIntAge(self):
        return (self.name, self.age)
    

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

humanNames = []

for name in humans:
    humanNames.append(name.getNameOnly())

print("List of All Names: ", humanNames)

a = [name for name in humanNames if name[0] == "D"]

print("Only names that start with 'D': ", a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

b = [name for name in humanNames if name[-1] == "e"]

print("Only names that end with 'e': ", b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

C_through_G = "CDEFG"

c = [name for name in humanNames if C_through_G.find(name[0]) >= 0]

print("Only names that start with a letter between 'C' and 'G', inclusive: ", c)

# Write a list comprehension that creates a list of all the ages plus 10.

humanAges = []

for age in humans:
    humanAges.append(age.getAgeOnly())

print("List of All Ages: ", humanAges)

d = [age_plus_ten+10 for age_plus_ten in humanAges]

print("List of All Ages Increased by 10:", d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.'

humanNamesAndAges = []

for nameAndAge in humans:
    humanNamesAndAges.append(nameAndAge.getNameAndAge())

print("List of All Ages AND Names: ", humanNamesAndAges)

hyphen = "-"

e = [hyphen.join(namePlusAge) for namePlusAge in humanNamesAndAges]

print("List of All Names JOINED with Ages (using a hyphen): ", e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

namesAndIntAges = []

for nameAndIntAge in humans:
    namesAndIntAges.append(nameAndIntAge.getNameAndIntAge())

print("List of All Names AND Integer Ages: ", namesAndIntAges)

tupleNamesAndIntAges = tuple(namesAndIntAges)

f = [specificAge for specificAge in tupleNamesAndIntAges if specificAge[1] >= 27 and specificAge[1] <= 32]

print("Tuple of All Names JOINED with Ages, between ages 27-32 (inclusive): ", f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.

g = [(f"<Human: {nameAndIntAgeEntry[0].upper()}, {nameAndIntAgeEntry[1]+5}>") for nameAndIntAgeEntry in namesAndIntAges]

print("List of All Names with Capitalized Letters and Ages Increased by 5: ", g)

# Write a list comprehension that contains the square root of all the ages.

# print("Square root of ages:")
# import math
# h = []
# print(h)
