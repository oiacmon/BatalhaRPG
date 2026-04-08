from Personagens.Personagens import Personagens

class Goblin(Personagens):
    def __init__(self):
        super().__init__(
            name="Goblin",
            health=80,
            damage=10,
            chance=70,
            image=  """
                goblin
                    """
        )

    ##def special_attack(self):
     ##   return self.damage *2  # ataque duplo