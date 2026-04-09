from Personagens.Personagens import Personagens
from random import randint

class Goblin(Personagens):
    def __init__(self):
        super().__init__(
            name="Goblin",
            health=100,
            damage=randint(15, 20),
            chance=100,
            image=  "Goblin"
        )

    ##def special_attack(self):
     ##   return self.damage *2  # ataque duplo