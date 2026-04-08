from Personagens.Personagens import Personagens

class Orc(Personagens):
    def __init__(self):
        super().__init__(
            name="Orc",
            health=120,
            damage=20,
            chance=60,
            image="or"
        )

    ##def special_attack(self):
      ##  return self.damage * 1.5