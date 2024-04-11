def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def simplificar_fracao(numerador, denominador):
    mdc = calcular_mdc(numerador, denominador)
    return numerador // mdc, denominador // mdc

def somar_fracao(p_numerador, p_denominador, q_numerador, q_denominador):
    denominador_comum = p_denominador * q_denominador
    novo_p_numerador = p_numerador * q_denominador
    novo_q_numerador = q_numerador * p_denominador
    novo_numerador = novo_p_numerador + novo_q_numerador
    return simplificar_fracao(novo_numerador, denominador_comum)

def subtrair_fracao(p_numerador, p_denominador, q_numerador, q_denominador):
    denominador_comum = p_denominador * q_denominador
    novo_p_numerador = p_numerador * q_denominador
    novo_q_numerador = q_numerador * p_denominador
    novo_numerador = novo_p_numerador - novo_q_numerador
    return simplificar_fracao(novo_numerador, denominador_comum)

def multiplicar_fracao(p_numerador, p_denominador, q_numerador, q_denominador):
    novo_numerador = p_numerador * q_numerador
    novo_denominador = p_denominador * q_denominador
    return simplificar_fracao(novo_numerador, novo_denominador)

def dividir_fracao(p_numerador, p_denominador, q_numerador, q_denominador):
    novo_numerador = p_numerador * q_denominador
    novo_denominador = p_denominador * q_numerador
    return simplificar_fracao(novo_numerador, novo_denominador)


    
p_numerador = int(input("Digite o numerador da primeira fração: "))
p_denominador = int(input("Digite o denominador da primeira fração: "))
q_numerador = int(input("Digite o numerador da segunda fração: "))
q_denominador = int(input("Digite o denominador da segunda fração: "))

    
p_numerador, p_denominador = simplificar_fracao(p_numerador, p_denominador)
q_numerador, q_denominador = simplificar_fracao(q_numerador, q_denominador)

   
soma = somar_fracao(p_numerador, p_denominador, q_numerador, q_denominador)
subtracao = subtrair_fracao(p_numerador, p_denominador, q_numerador, q_denominador)
produto = multiplicar_fracao(p_numerador, p_denominador, q_numerador, q_denominador)
quociente = dividir_fracao(p_numerador, p_denominador, q_numerador, q_denominador)

   
print(f'Soma das frações: {soma}')
print(f'Subtração das frações: {subtracao}')
print(f'Produto das frações: {produto}')
print(f'Quociente das frações: {quociente}')
