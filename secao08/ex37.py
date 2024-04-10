def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial
    
def hiper_fatorial(numero):
    hf = 1 
    for i in range(1, numero + 1):
        hf *= calcular_fatorial(i) ** i  
    return hf

numero = int(input("Digite um número inteiro: "))

print(hiper_fatorial(numero))
