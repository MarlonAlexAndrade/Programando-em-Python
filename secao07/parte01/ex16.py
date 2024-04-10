lista = [1, 2, 3, 4, 5]

opcao = 1

while opcao != 0:
    print("0- Sair")
    print("1- Mostrar o vetor na ordem direita: ")
    print("2- Mostrar o vetor na ordem inversa: ")

    opcao = int(input("Opção: "))

    if opcao == 1:
        print(lista)
        print("\n")
    elif opcao == 2:
        print(lista[::-1])
        print("\n")
    else:
        print("Digite um numero valido!")
        