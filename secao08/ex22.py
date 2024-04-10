def imprimir_padrao(caractere, n):
    for i in range(1, n + 1):
        linha = caractere * i
        print(linha)


caractere = input('Digite o caractere a ser impresso: ')
n = int(input('Digite o número de linhas: '))
imprimir_padrao(caractere, n)
