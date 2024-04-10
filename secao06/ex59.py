qtd_habitantes = int(input("Digite a quantidade de habitantes: "))
valor_kwh = float(input("Digite o valor do kwh: "))
media = 0
contador = 0
consumo_residencial = 0
consumo_comercial = 0
consumo_indutrial = 0
maior_consumo = float("-inf")
menor_consumo = float('inf')

for i in range(1, 100):
    consumo = float(input("Digite o consumo do mes: "))

    print("1- Residencial")
    print("2- Comercial")
    print("3- Industrial")
    print("4- Sair")
    opcao = int(input("Opção: "))

    if consumo > maior_consumo:
        maior_consumo = consumo

    elif consumo < menor_consumo:
        menor_consumo = consumo
    
    media += consumo
    contador += 1

    if opcao == 1:   
        consumo_residencial += 1
    elif opcao == 2:
        consumo_comercial += 1
    elif opcao == 3:
        consumo_indutrial += 1
    
    print(f'O habitante com o maior é {maior_consumo} e o menor é {menor_consumo}')
    print(f'A média do consumo dos habitantes é de {(media)/ (contador)}')
    print(f'O consumo residencial foi de {consumo_residencial}')
    print(f'O consumo residencial foi de {consumo_comercial}')
    print(f'O consumo residencial foi de {consumo_indutrial}')
