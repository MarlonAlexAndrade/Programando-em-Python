letra_maiuscula = "a"

while letra_maiuscula != 0:
    letra_maiuscula = input("Digite uma letra: ")
    numero_letras = ord(letra_maiuscula)   
    letra_minuscula = chr(numero_letras+32)
    print(letra_minuscula)
