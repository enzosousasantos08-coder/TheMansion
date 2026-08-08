import random

class Inimigo:
    def __init__(self, nome, vida, dano_min=10, dano_max=15, chance_acerto=70):
        self.nome = nome
        self.vida = vida
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.chance_acerto = chance_acerto

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida -= dano

    def atacar(self, alvo):
        acerto = random.randint(1, 100)
        if acerto <= self.chance_acerto:
            dano = random.randint(self.dano_min, self.dano_max)
            print(f"\nA criatura acerta e causa {dano} de dano!")
            alvo.receber_dano(dano)
        else:
            print("\nA criatura errou o ataque!")