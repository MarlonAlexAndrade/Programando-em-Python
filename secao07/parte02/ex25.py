def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i] == [jogador] * 3 or [tabuleiro[x][i] for x in range(3)] == [jogador] * 3:
            return True
    if [tabuleiro[x][x] for x in range(3)] == [jogador] * 3 or [tabuleiro[2-x][x] for x in range(3)] == [jogador] * 3:
        return True
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor == 0:
                return False  
    return True  

def proxima_jogada(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                temp_tabuleiro = [linha[:] for linha in tabuleiro]
                temp_tabuleiro[i][j] = -1
                if verificar_vitoria(temp_tabuleiro, -1):
                     return f"Próxima jogada do jogador -1: linha {i}, coluna {j}"
                tabuleiro[i][j] = 0

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                temp_tabuleiro = [linha[:] for linha in tabuleiro]
                temp_tabuleiro[i][j] = 1
                if verificar_vitoria(temp_tabuleiro, 1):
                    return f"Próxima jogada do jogador 1: linha {i}, coluna {j}"
                tabuleiro[i][j] = 0

    return "Não foi possível determinar a próxima jogada."

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jogador1 = True

while True:
    print('Escolha uma casa:')
    for valor in matriz:
        print(valor)
    print(proxima_jogada(matriz))
    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))
    print()

    if matriz[linha][coluna] == 0:
        matriz[linha][coluna] = -1 if jogador1 else 1
        jogador1 = not jogador1
    else:
        print("Digite um número válido!")

    for jogador in [-1, 1]:
        if verificar_vitoria(matriz, jogador):
            for valor in matriz:
                print(valor)
            print("Vitória do jogador", jogador)
            exit()

    if sum(1 for linha in matriz for valor in linha if valor == 0) == 0:
        print("Empate!")
        exit()
