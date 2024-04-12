def calcular_total_compra(nome_arquivo):
    total = 0
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome, preco = linha.strip().split(',')
            preco = float(preco)
            total += preco
    return total

nome_arquivo = input("Digite o nome do arquivo: ")
total_compra = calcular_total_compra(nome_arquivo)
print("O total da compra é:", total_compra)
