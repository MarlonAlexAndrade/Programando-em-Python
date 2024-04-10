sair = 0

while sair != 5:
    print("1- Adição")
    print("2- subtração")
    print("3- multiplicação")
    print("4- Divisão")
    print("5- Saída")

    opcao = int(input("Opção: "))

    numero01 = int(input("Digite o primeiro numero: "))
    numero02 = int(input("Digite o segundo numero: "))

    if opcao == 1:
        print(f'A soma dos numeros é de {numero01 + numero02}')
    elif opcao == 2:
        print(f'A subtração dos numeros é de {numero01 - numero02}')
    elif opcao == 3:
        print(f'A multiplicação dos numeros é de {numero01 * numero02}')
    elif opcao == 4:
        print(f'A divisao dos numeros é de {numero01 / numero02}')
    elif opcao == 5:
        sair =  5
    else:
        print("Digite um numero valido!")
        