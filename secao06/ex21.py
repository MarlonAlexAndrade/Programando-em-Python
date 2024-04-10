numero_inicio = int(input("Digite um numero inicial: "))
numero_final  = int(input("Digite um numero final: "))
soma = 0
multiplicacao = 1

for numero_inicio in range(numero_inicio, numero_final + 1):
    soma += numero_inicio
    multiplicacao *= numero_inicio

print(f'A soma dos numeros é de {soma}')
print(f'A multiplicação dos numeros é de {multiplicacao}')