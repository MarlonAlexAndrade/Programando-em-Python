def numeros_quadrados(lista01):
    numeros_quadrado = [num ** 2 for num in lista01]
    return numeros_quadrado


lista01 = []
lista02 = []

for i in range(0, 1):
    numero = int(input("Digite um numero: "))
    
    lista01.append(numero)
    lista02 = numeros_quadrados(lista01)

    print(lista01)
    print(lista02)


