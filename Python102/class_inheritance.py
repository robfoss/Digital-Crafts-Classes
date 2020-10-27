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

class Hero(Mob):
    def yell(self):
        print('Prepare to die!')
    super().get_hit()     

hero = Hero('Rob', 60, 6)
print(hero.power)

bad_guy = Mob('Baddy')
print(bad_guy.health)

hero.yell()
hero.attack(bad_guy)
