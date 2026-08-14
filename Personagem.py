class Personagem:
    def __init__(self, nome, vida, inventario=None):
        self.nome = nome
        self.vida = vida
        self.inventario = inventario if inventario is not None else []
        self.arma_equipada = None  # Equipando a faca como arma inicial

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > 100:
            self._vida = 100
        else:
            self._vida = valor

    
    def equipar_arma(self, arma):
        if self.quantidade_item(arma.nome) > 0:
            self.arma_equipada = arma
            print(f"\nVocê equipou a {arma.nome}.")
            return True
        print(f"\nVocê não possui a {arma.nome} no inventário.")
        return False
    def atacar(self, inimigo):
        if self.arma_equipada:
            self.arma_equipada.atacar(inimigo)
        else:
            print("\nVocê não tem uma arma equipada!")

        

    def adicionar_item(self, nome_item, tipo, quantidade=1):
        for item in self.inventario:
            if item["nome"] == nome_item:
                item["quantidade"] += quantidade
                print(f"\nVocê encontrou {quantidade} {nome_item}(s).")
                return
        self.inventario.append({"nome": nome_item, "tipo": tipo, "quantidade": quantidade})
        print(f"\nVocê encontrou {quantidade} {nome_item}(s).")


    def quantidade_item(self, nome_item):
        for item in self.inventario:
            if item["nome"] == nome_item:
                return item["quantidade"]
        return 0

    def usar_item(self, nome_item, quantidade=1):
        for item in self.inventario:
            if item["nome"] == nome_item and item["quantidade"] >= quantidade:
                item["quantidade"] -= quantidade
                return True
        return False

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"\nVocê recebeu {dano} de dano!")
        print(f"Vida atual: {self.vida}")

    def curar(self, quantidade):
        self.vida += quantidade
        if self.vida > 100:
            self.vida = 100
        print(f"\nVocê usa uma bandagem e recupera {quantidade} de vida!")

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_status(self):
        print('\n----------------------------')
        print(f'Vida: {self.vida}')

        if len(self.inventario) == 0:
            print('Inventário: vazio')
        else:
            print('Inventário:')
            for item in self.inventario:
                print(f"- {item['nome']} x{item['quantidade']}")

        print('----------------------------')