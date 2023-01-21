# Scope problem
# def update_health(amount):
    # health += amount

# health = 10
# print(health)
# update_health(20)
# print(health)
"""
The problem here is that to python health is a local variable and hence it is only accessible from 
the scope of the user defined function (update_health)  
To python the first instance of the variable health within the function and the instance outside
the function are two completely different variables 
You can fix this by making the health within the function global, although this is not the cleanest of remedies
"""


def update_health(amount):
    monster.health += amount


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        return new_energy

    def get_damage(self, damage):
        self.health -= damage

monster = Monster(100, 50)
print(monster.health)
monster.health += 20
print(monster.health)

# Showing how the function can now be used to update the health of the monster
# Showcases how the objects attributes can be updated pretty much anywhere in any scope
update_health(20)
print(monster.health)

monster.update_energy(20)
print(monster.energy)

"""
Create a hero class with 2 parameters: damage and monster
The monster call should have a method that lowers the Monsters health -> get_damage
The hero class should have an attack method that calls the get_damage method
The amount of damage should be hero.damage 
"""


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


hero = Hero(15, monster)
print(monster.health)
hero.attack()
print(monster.health)
