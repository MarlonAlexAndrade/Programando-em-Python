with open('arq.txt', 'r') as arquivo:
    contador = 0
    for linha in arquivo:
        for letra in linha:
            vogais = ['a', 'e', 'i', 'o', 'u']
            if letra.lower() in vogais:
                contador += 1

print(f'A quantidade de letras que são vogais é: {contador}')
