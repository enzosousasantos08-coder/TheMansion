import random
from dataclasses import dataclass

@dataclass
class Inimigo:
    nome: str
    vida: int
    dano_min: int = 10
    dano_max: int = 15
    chance_acerto: int = 70

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida -= dano

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