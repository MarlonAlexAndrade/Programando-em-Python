lista = []

for i in range(0, 10):
    numero = int(input("Digite um numero: "))
    
    lista.append(numero)

maior = max(lista)
index = lista.index(maior)

print(lista)
print(f'O maior numero é {maior} e o index dele é {index}')
