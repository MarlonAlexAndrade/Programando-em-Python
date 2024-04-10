numero = int(input("Digite um numero inteiro: "))

ultimo=1
penultimo=1

if (numero == 1) or (numero == 2):
    print("1")
else:
    soma = 0
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

        if fibonacci % 2 == 0:
            soma += fibonacci

    print(f'A soma dos pares é de {soma}')