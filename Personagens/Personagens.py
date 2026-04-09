import random

class Personagens:
    def __init__(self, name, health, damage, chance, image):
        self.name = name
        self.health = health
        self.damage = damage
        self.chance = chance
        self.image = image

    def attack(self):
        rolagem = random.randint(1, 100)
        if rolagem <= self.chance:
            return self.damage
        else:
            return 0