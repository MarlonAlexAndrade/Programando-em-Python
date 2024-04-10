numero = 1
maior_numero = float('-inf')

while numero > 0:
    numero = int(input("Digite um numero: "))

    if numero > maior_numero:
        maior_numero = numero

print(f'O maior numero digitado foi {maior_numero}')
