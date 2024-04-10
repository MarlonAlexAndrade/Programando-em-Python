def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def calcular_seno_hiperbolico(angulo_graus):
    angulo_radianos = angulo_graus * (3.141593 / 180) 
    seno_hiperbolico = 0
    for n in range(6): 
        termo = (angulo_radianos ** (2 * n + 1)) / calcular_fatorial(2 * n + 1)
        seno_hiperbolico += termo
    return seno_hiperbolico

angulo = float(input("Digite o valor do ângulo em graus (0 a 5): "))
resultado_seno_hiperbolico = calcular_seno_hiperbolico(angulo)
print(f'O seno hiperbólico de {angulo} graus é aproximadamente: {resultado_seno_hiperbolico}')
