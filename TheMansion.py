print('=== JOGO DE SOBREVIVENCIA ===')
print('Voce estava fugindo de criaturas na floresta, e se refugiou em uma mansão abandonada com seu grupo')

jogando = True
vida = 100
inventario = []
faca_pega = False
chave_pega = False

while jogando:
    print(f'\nVida: {vida} | Inventário: {inventario}')
    print('O que voce deseja fazer?')
    print('1 - Explorar a mansão')
    print('2 - Conversar com o grupo')
    print('3 - Sair do jogo')

    escolha = input('Digite o número da sua escolha: ')

    if escolha == "1":

        dentro_da_sala = True

        while dentro_da_sala:
         print(f'\nVida: {vida} | Inventário: {inventario}')
         if faca_pega == False:
          print('Voce vira a esquerda e se depara com uma sala de jantar chique com uma porta no fundo')
          print("Você encontra uma faca sobre a mesa e a guarda com você")
          inventario.append("faca")
          faca_pega = True
         else:
          print("A mesa está vazia. Você já pegou a faca.")
         print('O que você deseja fazer agora?')
         print('1 - Explorar a sala de jantar')
         print('2 - Abrir a porta no fundo da sala')
         escolha1 = input('Digite o número da sua escolha: ')
         if escolha1 == "1":
            if chave_pega == False:
                print("Você explora a sala de jantar e encontra uma chave em formato de caveira em cima da mesa principal")
                inventario.append("chave de caveira")
                chave_pega = True
            else:
                print("A mesa está vazia. Você já pegou a chave.")
         elif escolha1 == "2":
            print("Você abre a porta e se depara com um corredor escuro, você sente um cheiro estranho vindo do final do corredor")
            print("Você decide seguir em frente, mas de repente uma criatura aparece e te ataca!")
            print("Você consegue se defender com a faca, mas acaba se machucando no processo.")
            vida = vida - 20
            dentro_da_sala = False

        #futuramente irei adicionar a opção de explorar a sala por completo, antes de avançar

    elif escolha == "2":
        print("Você conversa com o grupo.")
        print("Um deles diz que não é seguro sair da mansão, então deveriam investigar a mansão enorme separadamente")
        #irei adicionar profundidade aos personagens futuramente

    elif escolha == "3":
        print("Você decide parar por aqui. Até a próxima!")
        jogando = False

    else:
        print("Voce ficou parado, o seu grupo foi explorar e agora voce esta sozinho, o silencio te incomoda")
        #ficar parado não é uma opção

    if vida <= 0:
        print("\nVocê não resistiu... FIM DE JOGO")
        jogando = False