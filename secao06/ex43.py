idade = 1
media = 0
contador = 0

while idade > 0:
    idade = int(input("Digite uma idade: "))
    media += idade
    contador += 1

print(f'O maior numero digitado foi {media / contador}')
