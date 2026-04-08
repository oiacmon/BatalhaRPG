from Personagens.Jogador import Jogador
from Personagens.RandomEnemy import get_random_enemy

def Partida():
    jogador = Jogador()
    inimigo = get_random_enemy()

    print(inimigo.image)
    print(f"Você encontrou um {inimigo.name} com {inimigo.health} de vida!")

    while True:
        if jogador.health <= 0:
            print("Você morreu!")
            break

        if inimigo.health <= 0:
            print(f"Você derrotou o {inimigo.name}!")
            break

        print("\nSua jogada:")
        acao = input("[A]tacar / [C]urar / [F]ugir: ").lower()

        if acao == "a":
            dano = jogador.atacar()
            inimigo.health -= dano
            print(f"Você causou {dano} de dano!")

        elif acao == "c":
            jogador.curar()

        elif acao == "f":
            print("Você fugiu!")
            break

        # Turno do inimigo
        dano_inimigo = inimigo.attack()
        jogador.health -= dano_inimigo
        print(f"O {inimigo.name} causou {dano_inimigo} de dano em você!")