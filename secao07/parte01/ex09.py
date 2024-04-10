pares = 0
lista = []

while pares != 6:
    numero = int(input("Digite um numero: "))
    
    if numero % 2 == 0:
        lista.append(numero) 
        pares += 1
    else:
        print("Digite um numero par")

lista_inversa = lista
lista_inversa.reverse()

print(lista_inversa)