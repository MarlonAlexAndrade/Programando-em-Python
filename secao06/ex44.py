numero = int(input("Digite um numero inteiro: "))

ultimo=1
penultimo=1

if (numero == 1) or (numero == 2):
    print("1")
else:
    contador = 0
    n = 0
    while contador <= 2:
        fibonacci = ultimo + penultimo
        penultimo = ultimo
        ultimo = fibonacci
        n += ultimo
        if n >= numero:
            contador += 1
        print(fibonacci)
    