from Personagens.Personagens import Personagens
from random import randint

class Golem(Personagens):
    def __init__(self):
        super().__init__(
            name="Golem",
            health=200,
            damage=randint(20,23),
            chance=50,
            image="Golem"
        )

    ##def special_defense(self):
      ##  return self.health * 0.1  # regenera 10% da vida