from Personagens.Personagens import Personagens
from random import randint
import random

class Goblin(Personagens):
    def __init__(self):
        super().__init__(
            name="Goblin",
            health=100,
            damage=randint(15, 20),
            chance=100,
            image="Goblin"
        )

    def defender(self, dano):
        chance_esquiva = 60
        rolagem = random.randint(1, 100)

        if rolagem <= chance_esquiva:
            print("⚡ O Goblin esquivou do seu ataque!")
            return 0

        return dano