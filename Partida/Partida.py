from Personagens.Jogador import Jogador
from Personagens.RandomEnemy import get_random_enemy
import random

def Partida():
    jogador = Jogador()
    inimigo = get_random_enemy()

    print(inimigo.image)
    print(f"Você encontrou um {inimigo.name} com {inimigo.health} de vida!")

    esquivando = False

    while True:
        if jogador.health <= 0:
            print("""
===========================================
Você morreu!
===========================================
                  """)
            break

        if inimigo.health <= 0:
            print(f"""
===========================================
Você derrotou o {inimigo.name}!
===========================================
                """)
            break

        print("\nSua jogada:")
        acao = input("[A]tacar / [C]urar / [E]squivar: ").lower()

        if acao == "a":
            dano = jogador.atacar()
            inimigo.health -= dano
            print(f"Você causou {dano} de dano!")
            esquivando = False

        elif acao == "c":
            jogador.curar()
            esquivando = False

        elif acao == "e":
            print("Você tenta esquivar do próximo ataque!")
            esquivando = True

        else:
            print("Ação inválida!")
            continue

        dano_inimigo = inimigo.attack()

        if esquivando:
            chance = random.randint(1, 100)
            if chance <= 40:
                print("Você conseguiu esquivar! Nenhum dano recebido!")
                dano_inimigo = 0
            else:
                print("Você falhou em esquivar!")
            esquivando = False

        jogador.health -= dano_inimigo
        print(f"O {inimigo.name} causou {dano_inimigo} de dano em você!")

        print(f"\n❤️ Sua vida: {jogador.health}")
        print(f"💀 Vida do {inimigo.name}: {inimigo.health}")