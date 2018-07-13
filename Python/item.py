import random

class Item:
    def __init__(self, name, healing, damage):
        self.name = name
        self.damage = damage
        self.healing = healing


items = [
    Item("Anti-Depressants", 0, 10),
    Item("Hell Trident", 5, 0),
    Item("Souls of the Innocent in a jar", 1, 5)
]

def getRandomItem():
    return random.choice(items)
