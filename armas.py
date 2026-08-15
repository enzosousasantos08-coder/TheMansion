

import random


class Arma:
    def __init__(self, nome, dano_min, dano_max, chance_acerto):
        self.nome = nome
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.chance_acerto = chance_acerto
    def atacar(self, alvo):
        acerto = random.randint(1, 100)
        if acerto <= self.chance_acerto:
            dano = random.randint(self.dano_min, self.dano_max)

            print(f"\nVocê acertou o ataque e causou {dano} de dano!")

            alvo.receber_dano(dano)
            return dano
        return 0
    
class Faca(Arma):
    def __init__(self):
        super().__init__(
            nome="faca",
            dano_min=10,
            dano_max=20,
            chance_acerto=80
        )


class Pistola(Arma):
    def __init__(self):
        super().__init__(
            nome="pistola",
            dano_min=25,
            dano_max=40,
            chance_acerto=70
        )


faca = Faca()
pistola = Pistola()

armas = {
    "faca": faca,
    "pistola": pistola
}

arma = armas.get("faca")