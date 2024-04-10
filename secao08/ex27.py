def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def calcular_seno(angulo_graus):
    angulo_radianos = angulo_graus * (3.141593 / 180)  
    seno = 0
    for n in range(6): 
        termo = ((-1) ** n) / calcular_fatorial(2 * n + 1) * (angulo_radianos ** (2 * n + 1))
        seno += termo
    return seno

angulo = float(input("Digite o valor do ângulo em graus (0 a 5): "))
resultado_seno = calcular_seno(angulo)
print(f'O seno de{angulo}, graus é aproximadamente: {resultado_seno}')
