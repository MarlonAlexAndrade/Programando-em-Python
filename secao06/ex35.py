numero_inicial = int(input("Digite um numero inicial: "))
numero_final = int(input("Digite um numero final: "))
soma = 0

if numero_final <= numero_inicial:
    print("Intevalo de valores inválido!")
else:
    for i in range(numero_inicial, numero_final):
        if i % 2 != 0:
            soma += i
        
    print(f'A soma dos numeros impares é de {soma}')