lista = []

for i in range(0, 10):
    numero = int(input("Digite um numero: "))

    if numero in lista:
        print("Digite um numero valido!")
    else:
         lista.append(numero)

print(lista)