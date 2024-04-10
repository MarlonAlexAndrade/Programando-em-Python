def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial
    
def super_fatorial(numero):
    sf = 1
    for i in range(numero+1):
        sf *= calcular_fatorial(i)
    
    return sf

numero = int(input("Digite um numero inteiro: "))

print(super_fatorial(numero))