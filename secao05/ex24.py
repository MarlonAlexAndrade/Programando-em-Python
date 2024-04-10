opcao = 1

while opcao != 0:
    valor = float(input("Digite o valor: "))
    print("\n")

    print("Escolha o Estado: ")
    print("1- MG.")
    print("2- SP.")
    print("3- RJ.")
    print("4- MS.")
    print("Caso desejar sair digite 0")

    opcao = int(input("Opção: "))

    if opcao == 1:
        valor_imposto = valor * 1.07  
        print (f'O valor com imposto é de {valor_imposto}')
    elif opcao == 2:
        valor_imposto = valor * 1.12  
        print (f'O valor com imposto é de {valor_imposto}')
    elif opcao == 3:
        valor_imposto = valor * 1.15  
        print (f'O valor com imposto é de {valor_imposto}')
    elif opcao == 4:
        valor_imposto = valor * 1.08  
        print (f'O valor com imposto é de {valor_imposto}')        
    else:
        print (f'Digite um numero valido!')
        
