opcao = 1

while opcao != 0:
    numero01 = float(input("Digite o primeiro numero: "))
    numero02 = float(input("Digite o segundo numero: "))
    print("\n")

    print("1- Soma de dois números.")
    print("2- Diferença entre dois números.")
    print("3- Produto entre dois numeros.")
    print("4- Divisão entre dois numeros.")
    print("Caso desejar sair digite 0")

    opcao = int(input("Opção: "))

    def switch(opcao):
        if opcao == 1:
            soma = numero01 + numero02
            return (f'A soma dos numeros é de {soma}')
        elif opcao == 2:
            diferenca = numero01 - numero02
            return (f'A diferença dos numeros é de {diferenca}')
        elif opcao == 3:
            produto = numero01 * numero02
            return (f'O produto dos numeros é de {produto}')
        elif opcao == 4:
            if numero02 != 0:
                dividir = numero01 / numero02
                return (f'A divisão dos numeros é de {dividir}')
            else:
                return (f'Digite um numero valido')
        else:
            return (f'Digite um numero valido!')
        
    print(switch(opcao))