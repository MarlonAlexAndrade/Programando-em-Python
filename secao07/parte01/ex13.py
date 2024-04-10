lista = []

for i in range(0, 5):
    numero = int(input("Digite um numero: "))
    
    lista.append(numero)

maior = max(lista)
index_maior = lista.index(maior)
menor = min(lista)
index_menor = lista.index(menor)

print(lista)
print(f'O maior numero é {maior} e o index dele é {index_maior}')
print(f'O menor numero é {menor} e o index dele é {index_menor}')
