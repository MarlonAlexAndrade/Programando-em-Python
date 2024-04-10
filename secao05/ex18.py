sair = 1

while sair != 0:
    numero01 = float(input("Digite o primeiro numero: "))
    numero02 = float(input("Digite o segundo numero: "))
    print("\n")

    print("Caso desejar somar digite 1")
    print("Caso desejar subtrair digite 2")
    print("Caso desejar multiplicar digite 3")
    print("Caso desejar dividir digite 4")
    print("Caso desejar sair digite 0")

    opcao = int(input("Opção: "))

    def switch(opcao):
        if opcao == 1:
            soma = numero01 + numero02
            return (f'A soma dos numeros é de {soma}')
        elif opcao == 2:
            subtrair = numero01 - numero02
            return (f'A subtração dos numeros é de {subtrair}')
        elif opcao == 3:
            multiplicar = numero01 * numero02
            return (f'A multiplicação dos numeros é de {multiplicar}')
        elif opcao == 4:
            dividir = numero01 / numero02
            return (f'A divisão dos numeros é de {dividir}')
        else:
            return (f'Digite um numero valido!')
        
    print(switch(opcao))





