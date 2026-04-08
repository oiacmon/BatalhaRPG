from Personagens.Personagens import Personagens

class Golem(Personagens):
    def __init__(self):
        super().__init__(
            name="Golem",
            health=200,
            damage=12,
            chance=40,
            image="go"
        )

    ##def special_defense(self):
      ##  return self.health * 0.1  # regenera 10% da vida