# =========================
# JOGO DE SOBREVIVÊNCIA
# =========================

print('=== JOGO DE SOBREVIVENCIA ===')

nome = input("\nQual é o seu nome? ")

print(f'\n{nome}, você estava fugindo de criaturas na floresta, e se refugiou em uma mansão abandonada com seu grupo')


# =========================
# VARIÁVEIS DO JOGO
# =========================

jogando = True
vida = 100
inventario = []
faca_pega = False
chave_pega = False


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

    print('----------------------------')


def conversar_grupo():

    print("\nVocê se reúne com o grupo na entrada da mansão.")

    print("\n1 - Conversar com Helena")
    print("2 - Conversar com Davi")
    print("3 - Voltar")

    conversa = input("Escolha com quem falar: ")

    if conversa == "1":
        print("\nHelena: Essa mansão é maior do que parece.")
        print("Helena: Acho que deveríamos explorar separadamente. Se ficarmos todos juntos, vamos perder muito tempo.")

    elif conversa == "2":
        print("\nDavi: Eu não gosto dessa ideia, mas não temos muitas opções.")
        print("Davi: Vamos dividir os caminhos e procurar qualquer coisa que possa nos ajudar.")
        print("Davi: Se encontrarmos algo estranho, voltamos imediatamente.")

    elif conversa == "3":
        print("\nVocê volta a investigar a mansão.")

    else:
        print("\nNinguém entendeu sua escolha.")


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
            print('1 - Explorar a sala de jantar')
            print('2 - Abrir a porta no fundo da sala')

            escolha1 = input('Digite o número da sua escolha: ')


            if escolha1 == "1":

                if chave_pega == False:

                    print("\nVocê explora a sala de jantar e encontra uma chave em formato de caveira em cima da mesa principal")

                    inventario.append("chave de caveira")
                    chave_pega = True

                else:

                    print("A mesa está vazia. Você já pegou a chave.")


            elif escolha1 == "2":

                print("\nVocê abre a porta e se depara com um corredor escuro.")
                print("Você sente um cheiro estranho vindo do final do corredor.")

                print("\nVocê decide seguir em frente, mas de repente uma criatura aparece e te ataca!")

                print("Você consegue se defender com a faca, mas acaba se machucando no processo.")

                vida = vida - 20
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