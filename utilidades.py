def pedir_escolha(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("\nEscolha inválida. Digite apenas números.")