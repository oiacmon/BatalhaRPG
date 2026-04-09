from Personagens.Personagens import Personagens
from random import randint

class Golem(Personagens):
    def __init__(self):
        super().__init__(
            name="Golem",
            health=200,
            damage=randint(20, 30),
            chance=70,
            image="Golem"
        )

    def defender(self, dano):
        reducao = int(dano * 0.4)
        dano_final = dano - reducao
        print("🪨 O Golem reduz parte do dano com sua armadura!")
        return dano_final