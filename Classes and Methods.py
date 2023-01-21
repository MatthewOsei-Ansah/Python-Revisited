# Passing a user defined function into a class

def add(a, b):
    return a + b


class Test:
    def __init__(self, add_function):
        self.add_function = add_function


test = Test(add)
print(test.add_function(1, 2))

"""
Exercise 1
Create a monster class with a parameter called func, store this func as a parameter
Create another class called attacks that has 4 methods:
bite, strike, slash, kick (each method just prints some text)
Create a monster object and give it one the attack methods from the attack class
"""


class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def bite(self):
        print("Bite")

    def strike(self):
        print("Strike")

    def slash(self):
        print("Slash")

    def kick(self):
        print("Kick")


monster = Monster(func=Attacks().bite)
monster.func()
