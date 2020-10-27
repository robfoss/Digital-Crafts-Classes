class Mob:
    def __init__(self, name, health = 10, power=2):
        self.name = name
        self.health = health
        self.power = power


    def get_hit(self, power):
        self.health = self.health - power
        print(f'I {self.name}, got hit for {power} points and now have {self.health}.')

    def attack(self, enemy):
        enemy.get_hit(self.power)

bad_guy = Mob('Mr. Evil',10, 2 )
hero = Mob('Rob', 30, 10)     
print(hero.health)

bad_guy.attack(hero)

hero.attack(bad_guy)
hero.attack(bad_guy)
hero.attack(bad_guy)

# Using our vehicle class from the previous lesson, add a speed, top_speed, position, and acceleration attribute.
# speed and position should start at 0, top_speed and acceleration are numbers.
# add a class method called move. When the move method is called have the position increase by the speed of the car.
# add a class method called accelerate and using the very simplified equation to have the vehicle accelerate when the accelerate method is called on that instance:
#  speed = speed + acceleration
# In the accelerate method, do not allow the vehicle to pass the top speed.
# modify the instances of the vehicles to include acceleration and top speed when you instance the vehicles.
# using a while loop and assuming each iteration of the loop is a 'second' have the vehicles 'race' by accelerating as much as possible on a drag strip for 20, 40, and 60 seconds to see who wins.
# (challange) instead of racing for a timeframe, make the race different distances. Position can be considered in meters.

class Vehicle:
    def __init__(self, speed = 0, top_speed = 0, acceleration = 0, wheels = 4):
        self.wheels = wheels
        self.top_speed = top_speed
        self.accerleration = acceleration
        self.position = 0
        self.speed = 0

    def move(self): 
        self.accelerate()
        self.position += self.speed

    def accelerate(self):
        self.speed += self.accerleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

all_cars = {
    'camero': Vehicle(100, 4),
    'volvo': Vehicle(80, 6),
    'focus': Vehicle(60, 5),
}

print('20 second run.')
for i in range(20):
    print(f'****Second {i}****')
    for car_name in all_cars:
        all_cars[car_name].move()

for car_name in all_cars:
    print(f'{car_name} - {all_cars[car_name].position}')    
