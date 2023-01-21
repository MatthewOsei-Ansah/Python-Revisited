"""
Dunder methods is just short for double underscore methods
They are not called by the user
It is instead called by python when something else happens
"""


class Monster:
    def __init__(self, health, energy):  # Whenever the class is called this is what is run first
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health  # No clue what the point of __len__ is here

    def __abs__(self):
        return self.energy  # Returns the value of energy as an absolute

    def __call__(self):
        print('The monster was called')  # Turns the class into a function returning something when it called

    def __add__(self, other):  # Self-explanatory
        return self.health + other

    def __str__(self):
       return 'A monster' # Allows stuff to return stuff as a string rather than a location in memory

    # Methods
    def attack(self, amount):
        print('The monster has been attacked')
        print(f'{amount} damage has been delt')
        self.energy -= 20
        print(f'The monster has {self.energy} left')


monster1 = Monster(20, 40)
monster2 = Monster(30, 50)

print(monster1.energy)
print(monster2.energy)

monster1.attack(100)

print(len(monster1))
print(abs(monster1))

# Returns all dunder methods as well as all the methods and attributes used
print(dir(monster1))

# Give all the attributes and methods as a dictionary
print(monster1.__dict__)
# Does the same thing
print(vars(monster1))

# Add method
print(monster1 + 20)

print(monster1)
