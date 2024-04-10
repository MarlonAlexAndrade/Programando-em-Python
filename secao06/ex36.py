quadrado = 0
soma = 0

for i in range(1, 101):
    quadrado += i ** 2
    soma += i

print(f'A soma dos quadrados dos cem primeiros numeros é {quadrado}, o quadrado da soma dos cem primeiros numeros é {soma ** 2}')