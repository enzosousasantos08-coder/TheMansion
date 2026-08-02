# =========================
# JOGO DE SOBREVIVÊNCIA
# =========================

print('=== JOGO DE SOBREVIVENCIA ===')

nome = input("\nQual é o seu nome? ")

print(f'\n{nome}, você estava fugindo de criaturas na floresta, e se refugiou em uma mansão abandonada com seu grupo')


# =========================
# VARIÁVEIS DO JOGO
# =========================

import random

jogando = True
vida = 100
inventario = []
faca_pega = False
chave_pega = False
conversa_personagemh = False
conversa_personagemd = False
mesa_explorada = False
municao = 0
bandagem = 0


# =========================
# FUNÇÕES
# =========================

def mostrar_status():
    print('\n----------------------------')
    print(f'Vida: {vida}')

    if len(inventario) == 0:
        print('Inventário: vazio')
    else:
        print('Inventário:')
        for item in inventario:
            print(f'- {item}')

    print(f'Munição: {municao}')
    print(f'Bandagens: {bandagem}')

    print('----------------------------')


def conversar_grupo():

    global conversa_personagemh, conversa_personagemd

    conversando = True

    while conversando:

     print("\nVocê se reúne com o grupo na entrada da mansão.")

     if conversa_personagemh == False:
      print("\n1 - Conversar com Helena")
    
     if conversa_personagemd == False:
      print("2 - Conversar com Davi")

     print("3 - Voltar")

     conversa = input("Escolha com quem falar: ")

     if conversa == "1" and conversa_personagemh == False:
        print("\nHelena: Essa mansão é maior do que parece.")
        print("Helena: Acho que deveríamos explorar separadamente. Se ficarmos todos juntos, vamos perder muito tempo.")
        conversa_personagemh = True

     elif conversa == "2" and conversa_personagemd == False:
        print("\nDavi: Eu não gosto dessa ideia, mas não temos muitas opções.")
        print("Davi: Vamos dividir os caminhos e procurar qualquer coisa que possa nos ajudar.")
        print("Davi: Se encontrarmos algo estranho, voltamos imediatamente.")
        conversa_personagemd = True

     elif conversa == "3":
        print("\nVocê volta a investigar a mansão.")
        conversando = False


     else:
        print("\nNinguém entendeu sua escolha.")

def receber_dano(dano):
    global vida

    vida = vida - dano

    print(f"\nVocê recebeu {dano} de dano!")
    print(f"Vida atual: {vida}")


# =========================
# MENU PRINCIPAL
# =========================

while jogando:

    mostrar_status()

    print('O que voce deseja fazer?')
    print('1 - Explorar a mansão')
    print('2 - Conversar com o grupo')
    print('3 - Sair do jogo')

    escolha = input('Digite o número da sua escolha: ')


    # =========================
    # EXPLORAR MANSÃO
    # =========================

    if escolha == "1":

        dentro_da_sala = True

        while dentro_da_sala:

            mostrar_status()

            if faca_pega == False:

                print('Voce vira a esquerda e se depara com uma sala de jantar chique com uma porta no fundo')
                print("Você encontra uma faca sobre a mesa e a guarda com você")

                inventario.append("faca")
                faca_pega = True

            else:

                print("A mesa está vazia. Você já pegou a faca.")


            print('\nO que você deseja fazer agora?')
            if chave_pega == False:
                print('1 - Explorar a sala de jantar')
            print('2 - Abrir a porta no fundo da sala')

            escolha1 = input('Digite o número da sua escolha: ')


            if escolha1 == "1" and mesa_explorada == False:

                print("\nVocê explora a sala de jantar e encontra uma chave em formato de caveira em cima da mesa principal")

                inventario.append("chave de caveira")

                item = random.randint(1,3)

                if item == 1:
                 inventario.append("munição")
                 municao += 3
                 print("Você encontrou 3 munições.")

                elif item == 2:
                 bandagem += 1
                 inventario.append("bandagem")
                
                 print("Você encontrou uma bandagem.")

                else:
                 print("Você não encontrou mais nada.")

                chave_pega = True
                mesa_explorada = True


            elif escolha1 == "2":

                print("\nVocê abre a porta e se depara com um corredor escuro.")
                print("Você sente um cheiro estranho vindo do final do corredor.")

                print("\nVocê decide seguir em frente, mas de repente uma criatura aparece e te ataca!")

                print("Você consegue se defender com a faca, mas acaba se machucando no processo.")

                receber_dano(20)

                vida_inimigo = 30
                
                while vida > 0 and vida_inimigo > 0:

                 print('o que você deseja fazer agora?')

                 print('1 - Atacar a criatura com a faca')
                 print('2 - Usar uma bandagem para se curar')

                 escolhaluta = input('Digite o número da sua escolha: ')

                 acerto = random.randint(1,100)

                 if escolhaluta == "1":
                  if acerto <= 80:
                   dano = random.randint(10, 20)
                   print(f"\nVocê acertou a criatura com a faca e causa {dano} de dano!")
                   vida_inimigo -= dano
                  else:
                   print("\nVocê errou o ataque!")

                 elif escolhaluta == "2":
                     if bandagem > 0:
                         bandagem -= 1
                         vida += 40
                         if vida > 100:
                             vida = 100

                         print(f"\nVocê usa uma bandagem e recupera 40 de vida!")
                     else:
                         print("\nVocê não tem bandagens suficientes.")
                 else:
                                    print("\nOpção inválida.")

                 # ATAQUE DO INIMIGO
                 if vida_inimigo > 0:
                   
                   acerto_inimigo = random.randint(1,100)
                   if acerto_inimigo <= 70:
                    dano_inimigo = random.randint(10, 15)
                    print(f"\nA criatura acerta e causa {dano_inimigo} de dano!")
                    receber_dano(dano_inimigo)
                   else:
                    print("\nA criatura errou o ataque!")

                 if vida_inimigo <= 0:
                     print("\nVocê derrotou a criatura")

                # EXPLORAÇÃO
                     print('A criatura cai no chão, e voce decide continuar explorando o corredor e ve duas portas a esquerda')
                     print('O que você deseja fazer agora?')
                     print('1 - Abrir a primeira porta')
                     print('2 - Abrir a segunda porta')

                     escolha_porta = input('Digite o número da sua escolha: ')
                     if escolha_porta == "1":
                        print("\nVocê abre a porta e encontra um quarto antigo com móveis cobertos de poeira. Parece que ninguém entrou aqui há muito tempo.")
                        print("Você encontra uma bandagem em cima da cama e a guarda com você.")
                        bandagem += 1
                        inventario.append("bandagem")
                     elif escolha_porta == "2":
                        print("\nVocê abre a porta e encontra um pequeno escritório com uma escrivaninha com gavetas e algumas estantes de livros.")
                        print("Você encontra uma munição em cima da escrivaninha e a guarda com você.")
                        municao += 1
                        inventario.append("munição")
                     dentro_da_sala = False

            
                 




    # =========================
    # CONVERSAR COM O GRUPO
    # =========================

    elif escolha == "2":

        conversar_grupo()



    # =========================
    # SAIR DO JOGO
    # =========================

    elif escolha == "3":

        print("\nVocê decide parar por aqui. Até a próxima!")
        jogando = False



    else:

        print("\nVocê ficou parado, o seu grupo foi explorar e agora voce esta sozinho, o silencio te incomoda")



    # =========================
    # MORTE
    # =========================

    if vida <= 0:

        print("\nVocê não resistiu... FIM DE JOGO")
        jogando = False