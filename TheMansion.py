print('=== JOGO DE SOBREVIVENCIA ===')
print('Voce estava fugindo de criaturas na floresta, e se refugiou em uma mansão abandonada com seu grupo')

jogando = True
vida = 100
inventario = []

while jogando:
    print(f'\nVida: {vida} | Inventário: {inventario}')
    print('O que voce deseja fazer?')
    print('1 - Explorar a mansão')
    print('2 - Conversar com o grupo')
    print('3 - Sair do jogo')

    escolha = input('Digite o número da sua escolha: ')

    if escolha == "1":
        print("Você segue pela esquerda e se depara com uma sala grande e chique de jantar, com uma porta no fundo")
        print("Você encontra uma faca sobre a mesa e a guarda com você")
        inventario.append("faca")
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