from Personagens.Personagens import Personagens

class Jogador(Personagens):
    def __init__(self):
        super().__init__(
            name="Jogador",
            health=120,
            damage=15,
            chance=80,
            image=
            """
            ---------------------
            |
            |
            |
            |
            |
            |
            ----------------------
            """
        )

    def curar(self):
        self.health += 20
        print("Você recuperou 20 de vida!")

    def atacar(self):
        return self.damage