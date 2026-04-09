from Personagens.Personagens import Personagens
from random import randint
import random

class Orc(Personagens):
    def __init__(self):
        super().__init__(
            name="Orc",
            health=150,
            damage=randint(20, 25),
            chance=80,
            image="Orc"
        )
        self.furia = False

    def defender(self, dano):
        if random.randint(1, 100) <= 40:
            print("🔥 O Orc entrou em fúria!")
            self.furia = True
            return int(dano * 0.5)
        return dano

    def attack(self):
        dano = super().attack()
        if self.furia:
            print("💢 O Orc ataca com fúria!")
            self.furia = False
            return dano * 2
        return dano