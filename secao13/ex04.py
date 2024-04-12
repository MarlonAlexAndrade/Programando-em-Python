with open('arq.txt', 'r') as arquivo:
    qtd_vogais = 0
    qtd_consoantes = 0
    for linha in arquivo:
        for letra in linha:
            vogais = ['a', 'e', 'i', 'o', 'u']
            consoantes = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
            if letra.lower() in vogais:
                qtd_vogais += 1
            if letra.lower() in consoantes:
                qtd_consoantes += 1

print(f'A quantidade de letras que são vogais é: {qtd_vogais}')
print(f'A quantidade de letras que são consoantes é: {qtd_consoantes}')
