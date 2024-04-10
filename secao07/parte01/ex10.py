notas = 0
lista = []

while notas != 6:
    numero = int(input("Digite um numero: "))

    if numero >= 0 and numero <= 10:
        lista.append(numero) 
        notas += 1
    else:
        print("Digite um numero valido")

soma = sum(lista)
media = soma / notas

print(f'A media geral dos alunos ficou em {media}')
