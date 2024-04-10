import math

opcao = "a"

while opcao != "e":
    nota01 = float(input("Digite a primeira notar: "))
    nota02 = float(input("Digite a segunda notar: "))
    nota03 = float(input("Digite a terceira notar: "))
    print("\n")

    print("Escolha o Estado: ")
    print("(A)- Geométrica.")
    print("(B)- Ponderada.")
    print("(C)- Harmônica.")
    print("(D)- Aritmética.")
    print("(E)- Caso desejar sair")

    opcao = input("Opção: ")

    if opcao == "A":
        geometrica = nota01 * nota02 * nota03 
        print(f'A média geométrica é de {math.pow(geometrica, 1/3)}') 
    elif opcao == "B":
        ponderada = ((nota01 * 2) + (nota02 * 2) + (nota03 * 6) / 3)
        print(f'A média ponderada é {ponderada}')
    elif opcao == "C":
        harmonica = [1 / nota01, 1 / nota02, 1 / nota03]
        soma_inversos = sum(harmonica)
        print(f'A média harmonica é de {3 / soma_inversos}') 
    elif opcao == "D":
        aritmetica = (nota01 + nota02 + nota03) / 3
        print(f'A média aritmética é {aritmetica}')       
    else:
        print (f'Digite um numero valido!')
        
