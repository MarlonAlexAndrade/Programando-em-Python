def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def calcular_cosseno(angulo_graus):
    angulo_radianos = angulo_graus * (3.141593 / 180)  
    cosseno = 0
    for n in range(6): 
        termo = ((-1) ** n) / calcular_fatorial(2 * n) * (angulo_radianos ** (2 * n))
        cosseno += termo
    return cosseno

angulo = float(input("Digite o valor do ângulo em graus (0 a 5): "))
resultado_cosseno = calcular_cosseno(angulo)
print(f'O seno de {angulo} graus é aproximadamente: {resultado_cosseno}')
