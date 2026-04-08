class Personagens:
    def __init__(self, name, health, damage, chance, image):
        self.name = name
        self.health = health
        self.damage = damage
        self.chance = chance
        self.image = image

    def attack(self):
        return self.damage