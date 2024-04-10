def ler_matriz():
    matriz = []
    for i in range(2):
        linha = []
        for j in range(2):
            valor = float(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz01, matriz02):
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            linha.append(matriz01[i][j] + matriz02[i][j])
        resultado.append(linha)
    return resultado

def subtrair_matrizes(matriz01, matriz02):
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            linha.append(matriz01[i][j] - matriz02[i][j])
        resultado.append(linha)
    return resultado

def adicionar_constante(matriz, constante):
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            linha.append(matriz[i][j] + constante)
        resultado.append(linha)
    return resultado

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

print("Digite os valores da primeira matriz:")
matriz01 = ler_matriz()

print("\nDigite os valores da segunda matriz:")
matriz02 = ler_matriz()

while True:
    print("\nMenu de Opções:")
    print("a) Somar as duas matrizes")
    print("b) Subtrair a primeira matriz da segunda")
    print("c) Adicionar uma constante às duas matrizes")
    print("d) Imprimir as matrizes")
    print("e) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == 'a':
        resultado = somar_matrizes(matriz01, matriz02)
        print("\nResultado da soma das matrizes:")
        imprimir_matriz(resultado)
    elif opcao == 'b':
        resultado = subtrair_matrizes(matriz02, matriz01)
        print("\nResultado da subtração das matrizes (segunda - primeira):")
        imprimir_matriz(resultado)
    elif opcao == 'c':
        constante = float(input("Digite a constante a ser adicionada às matrizes: "))
        matriz01_adicionada = adicionar_constante(matriz01, constante)
        matriz02_adicionada = adicionar_constante(matriz02, constante)
        print("\nMatriz 1 com a constante adicionada:")
        imprimir_matriz(matriz01_adicionada)
        print("\nMatriz 2 com a constante adicionada:")
        imprimir_matriz(matriz02_adicionada)
    elif opcao == 'd':
        print("\nMatriz 1:")
        imprimir_matriz(matriz01)
        print("\nMatriz 2:")
        imprimir_matriz(matriz02)
    elif opcao == 'e':
        print("Programa Encerrado!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
