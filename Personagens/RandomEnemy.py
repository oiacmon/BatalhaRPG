from random import choice

from Personagens.Goblin import Goblin
from Personagens.Orc import Orc
from Personagens.Golem import Golem

def get_random_enemy():
    enemy_classes = [Goblin, Orc, Golem]
    enemymath = choice(enemy_classes)()
    return enemymath