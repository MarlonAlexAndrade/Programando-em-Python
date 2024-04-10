codigo = 1

while codigo != 0:
    quantidade = float(input("Digite a quantidade: "))
    print("\n")

    print("Escolha o Lanche: ")
    print("Descrição       |Código | Preço")
    print("Cachorro Quente | 100   | 1.20")
    print("Bauru Simples   | 101   | 1.30")
    print("Bauru com Ovo   | 102   | 1.50")
    print("Hamburguer      | 103   | 1.20")
    print("Cheeseburguer   | 104   | 1.70")
    print("Suco            | 105   | 2.20")
    print("Refrigerante    | 106   | 1.00")
    print("Caso desejar sair digite 0")

    codigo = int(input("Opção: "))

    if codigo == 100:
        print(f'O valor total fica {quantidade * 1.20}')
    elif codigo == 101:
        print(f'O valor total fica {quantidade * 1.30}')
    elif codigo == 102:
        print(f'O valor total fica {quantidade * 1.50}')
    elif codigo == 103:
        print(f'O valor total fica {quantidade * 1.20}')
    elif codigo == 104:
        print(f'O valor total fica {quantidade * 1.70}')
    elif codigo == 105:
        print(f'O valor total fica {quantidade * 2.20}')
    elif codigo == 106:
       print(f'O valor total fica {quantidade * 1.00}')
    else:
        print (f'Digite um codigo valido!')
        
