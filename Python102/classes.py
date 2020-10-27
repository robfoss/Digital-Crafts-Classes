class Person:
    def __init__(self, name, age, height="normal"):
        print(f'You\'ve created a new instance of person')
        self.name = name
        self.age = age
        self.height = height

# instantiate that act of creating an instance. object is the instance of a class.
# attribute
rob = Person('Rob', 31, 'average')
erikka = Person('Erikka', 30)

print(rob.height)


# Create a program that has a class named Vehicle.
# Mae the Vehicle have a 'category' which can be anything like, sport, truck, motorcycle, minivan.
# Make the Vehicle class have 'wheels' as an attribute.
# Make the Vehicle class have 4 as the default value for the class.
# Create 5 different instances of the class with at least one being a motorcycle.

class Vehicle:
    def __init__(self, category, wheels = 4):
        self.category = category
        self.wheels = wheels

mustang = Vehicle('sports car')
accord = Vehicle('sedan')
tesla = Vehicle('electric')
motorcycle = Vehicle('sports', 2)
corvette = Vehicle('sports car')

print(corvette.wheels)
