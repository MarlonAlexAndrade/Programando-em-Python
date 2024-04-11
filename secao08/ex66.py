def upper_letras(letra):
    numero_letras = ord(letra)   

    if 65 <= numero_letras <= 90:
        return letra
    
    letra_maiuscula = chr(numero_letras-32)

    return letra_maiuscula


letra = input("Digite uma letra: ")

print(f'Letra em maiusculo : {upper_letras(letra)}')
