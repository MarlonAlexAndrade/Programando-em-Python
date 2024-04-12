alfabeto = {letra: 0 for letra in 'abcdefghijklmnopqrstuvwxyz'}

with open('arq.txt', 'r') as arquivo:
    qtd_caracter = 0
    for linha in arquivo:
        for letra in linha:         
            if letra.lower() in alfabeto:
                alfabeto[letra] += 1

print(f'A quantidade de caracter no arquivo é de: {alfabeto}')
