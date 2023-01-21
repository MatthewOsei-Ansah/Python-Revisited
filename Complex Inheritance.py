class Monster:
    #  The **kwargs allows extra arguments to be stored in a separate dictionary
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        # Allows the following class in the order of methods to be called
        super().__init__(**kwargs)

    # Methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')


class Fish:
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')


class Shark(Monster, Fish):
    def __init__(self, bite_strength, shark_health, shark_energy, speed, has_scales):
        # If you are using kwargs then everything has to be converted to a keyword argument as seen below
        super().__init__(health=shark_health, energy=shark_energy, speed=speed, has_scales=has_scales)
        self.bite_strength = bite_strength


#  MRO Method Resolution Order. It shows it what order python is going to go through the classes
#  print(Shark.mro())

shark = Shark(50, 150, 200, 100, False)
print(shark.speed)
