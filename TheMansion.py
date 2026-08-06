import random

# =========================
# CLASSES (POO de verdade)
# =========================
# Antes: vida, inventario e funções soltas usando "global"
# Agora: tudo isso vive DENTRO da classe Personagem, como atributos (self.vida,
# self.inventario) e métodos (self.receber_dano(), self.usar_item()...).
# Isso evita precisar de "global" e deixa o código mais organizado.

class Personagem:
    def __init__(self, nome, vida, inventario=None):
        self.nome = nome
        self.vida = vida
        self.inventario = inventario if inventario is not None else []
        self.arma_equipada = None  # Equipando a faca como arma inicial
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
            print(f"\nVocê acertou a criatura com a {self.nome} e causou {dano} de dano!")
            alvo.receber_dano(dano)
        else:
            print(f"\nVocê errou o ataque com a {self.nome}!")
faca = Arma("Faca", dano_min=10, dano_max=20, chance_acerto=80)

pistola = Arma("Pistola", dano_min=25, dano_max=40, chance_acerto=70)

   


# =========================
# FUNÇÕES DE JOGO (usam os objetos, não variáveis globais de vida/inventário)
# =========================

def combate(jogador, inimigo):
    while jogador.esta_vivo() and inimigo.esta_vivo():

        print("\nO que você deseja fazer agora?")
        print("1 - Atacar com a faca")
        print("2 - Usar bandagem")

        escolhaluta = input("Digite o número da sua escolha: ")

        if escolhaluta == "1":
                jogador.atacar(inimigo)
            
        elif escolhaluta == "2":
            if jogador.usar_item("bandagem"):
                jogador.curar(40)
            else:
                print("\nVocê não tem bandagens suficientes.")

        else:
            print("\nOpção inválida.")

        if inimigo.esta_vivo():
            inimigo.atacar(jogador)

    return not inimigo.esta_vivo()


def conversar_grupo(estado):
    conversando = True

    while conversando:
        print("\nVocê se reúne com o grupo na entrada da mansão.")

        if not estado["conversa_helena"]:
            print("\n1 - Conversar com Helena")
        if not estado["conversa_davi"]:
            print("2 - Conversar com Davi")
        print("3 - Voltar")

        conversa = input("Escolha com quem falar: ")

        if conversa == "1" and not estado["conversa_helena"]:
            print("\nHelena: Essa mansão é maior do que parece.")
            print("Helena: Acho que deveríamos explorar separadamente. Se ficarmos todos juntos, vamos perder muito tempo.")
            estado["conversa_helena"] = True
        elif conversa == "2" and not estado["conversa_davi"]:
            print("\nDavi: Eu não gosto dessa ideia, mas não temos muitas opções.")
            print("Davi: Vamos dividir os caminhos e procurar qualquer coisa que possa nos ajudar.")
            print("Davi: Se encontrarmos algo estranho, voltamos imediatamente.")
            estado["conversa_davi"] = True
        elif conversa == "3":
            print("\nVocê volta a investigar a mansão.")
            conversando = False
        else:
            print("\nNinguém entendeu sua escolha.")


# =========================
# INTRODUÇÃO
# =========================

print('=== JOGO DE SOBREVIVENCIA ===')
nome = input("\nQual é o seu nome? ")
print(f'\n{nome}, você estava fugindo de criaturas na floresta, e se refugiou em uma mansão abandonada com seu grupo')

# Antes: vida = 100, inventario = [] soltos.
# Agora: tudo isso é o próprio objeto "jogador".
jogador = Personagem(nome, vida=100)

# Estado do jogo que não pertence ao personagem (flags de progresso da história)
estado = {
    "faca_pega": False,
    "chave_pega": False,
    "conversa_helena": False,
    "conversa_davi": False,
    "mesa_explorada": False,
}

jogando = True

# =========================
# MENU PRINCIPAL
# =========================

while jogando:
    jogador.mostrar_status()

    print('O que voce deseja fazer?')
    print('1 - Explorar a mansão')
    print('2 - Conversar com o grupo')
    print('3 - Sair do jogo')

    escolha = input('Digite o número da sua escolha: ')

    if escolha == "1":
        dentro_da_sala = True

        while dentro_da_sala:
            jogador.mostrar_status()

            if not estado["faca_pega"]:
                print('Voce vira a esquerda e se depara com uma sala de jantar chique com uma porta no fundo')
                print("Você encontra uma faca sobre a mesa e a guarda com você")
                jogador.adicionar_item("faca", "arma")
                jogador.equipar_arma(faca)  
                estado["faca_pega"] = True
            else:
                print("A mesa está vazia. Você já pegou a faca.")

            print('\nO que você deseja fazer agora?')
            if not estado["chave_pega"]:
                print('1 - Explorar a sala de jantar')
            print('2 - Abrir a porta no fundo da sala')

            escolha1 = input('Digite o número da sua escolha: ')

            if escolha1 == "1" and not estado["mesa_explorada"]:
                print("\nVocê explora a sala de jantar e encontra uma chave em formato de caveira em cima da mesa principal")
                jogador.adicionar_item("chave de caveira", "chave")

                item = random.randint(1, 3)
                if item == 1:
                    jogador.adicionar_item("pistola", "arma")
                    jogador.adicionar_item("munição", "munição", 3)
                elif item == 2:
                    jogador.adicionar_item("bandagem", "cura")
                else:
                    print("Você não encontrou mais nada.")

                estado["chave_pega"] = True
                estado["mesa_explorada"] = True

            elif escolha1 == "2":
                print("\nVocê abre a porta e se depara com um corredor escuro.")
                print("Você sente um cheiro estranho vindo do final do corredor.")
                print("\nVocê decide seguir em frente, mas de repente uma criatura aparece e te ataca!")
                print("Você consegue se defender com a faca, mas acaba se machucando no processo.")

                jogador.receber_dano(20)
                zumbi = Inimigo("Zumbi", vida=30)
                venceu = combate(jogador, zumbi)

                if venceu:
                    print("\nVocê derrotou a criatura")
                    print('A criatura cai no chão, e voce decide continuar explorando o corredor e ve duas portas a esquerda')
                    print('O que você deseja fazer agora?')
                    print('1 - Abrir a primeira porta')
                    print('2 - Abrir a segunda porta')

                    escolha_porta = input('Digite o número da sua escolha: ')

                    if escolha_porta == "1":
                        print("\nVocê abre a porta e encontra um quarto antigo com móveis cobertos de poeira. Parece que ninguém entrou aqui há muito tempo.")
                        print("Você encontra uma bandagem em cima da cama e a guarda com você.")
                        jogador.adicionar_item("bandagem", "cura")
                    elif escolha_porta == "2":
                        print("\nVocê abre a porta e encontra um pequeno escritório com uma escrivaninha com gavetas e algumas estantes de livros.")
                        print("Você encontra uma munição em cima da escrivaninha e a guarda com você.")
                        jogador.adicionar_item("munição", "arma")

                dentro_da_sala = False

    elif escolha == "2":
        conversar_grupo(estado)

    elif escolha == "3":
        print("\nVocê decide parar por aqui. Até a próxima!")
        jogando = False

    else:
        print("\nVocê ficou parado, o seu grupo foi explorar e agora voce esta sozinho, o silencio te incomoda")

    if not jogador.esta_vivo():
        print("\nVocê não resistiu... FIM DE JOGO")
        jogando = False