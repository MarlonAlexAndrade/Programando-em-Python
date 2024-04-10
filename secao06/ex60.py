soma = 0
media_pares = 0
contador = 0
maior_numero = float("-inf")
menor_numero = float('inf')
numero = 1

while numero > 0:
    numero = float(input("Digite um numero: "))

    if numero > maior_numero:
        maior_numero = numero

    elif numero < menor_numero:
        menor_numero = numero
    
    soma += numero
    contador += 1

    if numero % 2 == 0:
        media_pares += numero
    
    print(f'O maior numero é {maior_numero} e o menor é {menor_numero}')
    print(f'Foram digitados {contador} numeros ')
    print(f'A média dos numeros é de {soma/ contador}')
    print(f'A media dos numeros pares é de {media_pares / contador}')
