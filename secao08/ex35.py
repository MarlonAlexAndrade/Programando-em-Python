def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def fatorial_quadruplo(numero):
    fatorial = calcular_fatorial(2*numero) // calcular_fatorial(numero)  

    return fatorial
    
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

print(fatorial_quadruplo(numero))
