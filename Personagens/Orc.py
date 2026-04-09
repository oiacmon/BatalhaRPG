from Personagens.Personagens import Personagens
from random import randint

class Orc(Personagens):
    def __init__(self):
        super().__init__(
            name="Orc",
            health=120,
            damage=randint(18,20),
            chance=80,
            image="Orc"
        )

    ##def special_attack(self):
      ##  return self.damage * 1.5