lista = []

for i in range(0, 5):
    numero = int(input("Digite um numero: "))
    
    lista.append(numero)

maior = max(lista)
menor = min(lista)
soma = sum(lista)
quantidade = len(lista)

media = soma / quantidade

print(lista)
print(f'O maior numero é {maior} e o menor numero é {menor}, e a media dos numeros da lista é {media}')
