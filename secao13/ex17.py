def ler_arquivo_matriz(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dimensoes = tuple(map(int, arquivo.readline().split()))
        qtd_anuladas = arquivo.readline()
        posicoes_anuladas = [tuple(map(int, linha.split())) for linha in arquivo.readlines()]
    return dimensoes, posicoes_anuladas

def gerar_matriz(dimensoes, posicoes_anuladas):
    matriz = [[1] * dimensoes[1] for _ in range(dimensoes[0])]
    for linha, coluna in posicoes_anuladas:
        matriz[linha][coluna] = 0
    return matriz

def escrever_matriz(nome_arquivo, matriz):
    with open(nome_arquivo, 'w') as arquivo:
        for linha in matriz:
            arquivo.write(' '.join(map(str, linha)) + '\n')

nome_arquivo = "matriz.txt"
dimensoes, posicoes_anuladas = ler_arquivo_matriz(nome_arquivo)

matriz = gerar_matriz(dimensoes, posicoes_anuladas)

nome_arquivo_saida = "matriz_saida.txt"
escrever_matriz(nome_arquivo_saida, matriz)

print("Matriz processada e escrita no arquivo de saída com sucesso!")
