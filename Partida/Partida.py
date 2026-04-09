from Personagens.Jogador import Jogador
from Personagens.RandomEnemy import get_random_enemy
import random

def Partida():
    jogador = Jogador()
    inimigo = get_random_enemy()

    print(inimigo.image)
    print(f"Você encontrou um {inimigo.name} com {inimigo.health} de vida!")

    esquivando = False
    buff_esquiva = False

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

            if buff_esquiva:
                dano = int(dano * 1.5)
                print("Você atacou com bônus da esquiva!")
                buff_esquiva = False

            dano = inimigo.defender(dano)
            inimigo.health -= dano
            print(f"Você causou {dano} de dano!")
            esquivando = False

        elif acao == "c":
            if buff_esquiva:
                print("Sua cura foi fortalecida pela esquiva!")
                jogador.health += float(jogador.curar() * 1.5)
                buff_esquiva = False
            else:
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
            if random.randint(1, 100) <= 50:
                print("Você conseguiu esquivar! Nenhum dano recebido!")
                dano_inimigo = 0
                buff_esquiva = True
            else:
                print("Você falhou em esquivar!")
            esquivando = False

        jogador.health -= dano_inimigo
        print(f"O {inimigo.name} causou {dano_inimigo} de dano em você!")

        print(f"\n❤️ Sua vida: {jogador.health}")
        print(f"💀 Vida do {inimigo.name}: {inimigo.health}")