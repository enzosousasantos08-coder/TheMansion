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