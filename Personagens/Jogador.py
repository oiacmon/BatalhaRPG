from Personagens.Personagens import Personagens
from random import randint

class Jogador(Personagens):
    def __init__(self):
        super().__init__(
            name="Jogador",
            health=100,
            damage=15,
            chance=70,
            image=
            """
            """
        )

    def curar(self):
        cura = randint(15, 25)
        self.health += cura
        print(f"Você recuperou {cura} de vida!")
        return cura

    def atacar(self):
        self.damage = randint(15, 25)
        return self.damage