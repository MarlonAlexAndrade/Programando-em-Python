with open('arq.txt', 'r') as arquivo:
    qtd_caracter = 0
    for linha in arquivo:
        for letra in linha:
            caractere = 'c'
            if letra.lower() == 'c':
                qtd_caracter += 1

print(f'A quantidade de caracter {caractere} no arquivo é de: {qtd_caracter}')
