numero_inicial = int(input("Digite o numero inicial: "))
numero_final = int(input("Digite o numero final: "))

soma = 0

if numero_inicial < 2 : 
    print("Digite um numero maior que 1")   
else:
    while numero_inicial < numero_final:        
        if numero_inicial % 2 != 0:
            print(numero_inicial)
            soma += numero_inicial
        numero_inicial += 1
    
    print(f'A soma dos numeros primos entre o intervalo é de {soma}')