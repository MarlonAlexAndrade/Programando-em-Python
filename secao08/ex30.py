def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def calcular_cosseno_hiperbolico(angulo_graus):
    angulo_radianos = angulo_graus * (3.141593 / 180) 
    cosseno_hiperbolico = 0
    for n in range(6):  
        termo = (angulo_radianos ** (2 * n)) / calcular_fatorial(2 * n)
        cosseno_hiperbolico += termo
    return cosseno_hiperbolico

angulo = float(input("Digite o valor do ângulo em graus (0 a 5): "))
resultado_cosseno_hiperbolico = calcular_cosseno_hiperbolico(angulo)
print(f'O cosseno hiperbólico de {angulo} graus é aproximadamente: {resultado_cosseno_hiperbolico}')
