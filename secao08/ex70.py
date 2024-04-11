def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def reduz(a, b):
    mdc = calcular_mdc(a, b)
    return a // mdc, b // mdc

def neg(x):
    return -x[0], x[1]

def soma(x, y):
    numerador = x[0] * y[1] + y[0] * x[1]
    denominador = x[1] * y[1]
    return reduz(numerador, denominador)

def mult(x, y):
    numerador = x[0] * y[0]
    denominador = x[1] * y[1]
    return reduz(numerador, denominador)

def div(x, y):
    numerador = x[0] * y[1]
    denominador = x[1] * y[0]
    return reduz(numerador, denominador)


rac1 = reduz(3, 6)
rac2 = reduz(2, 5)

print(f"Racional 1: {rac1}")
print(f"Racional 2: {rac2}")

print(f"Negativo de rac1: {neg(rac1)}")
print(f"Soma de rac1 e rac2: {soma(rac1, rac2)}")
print(f"Multiplicação de rac1 e rac2: {mult(rac1, rac2)}")
print(f"Divisão de rac1 por rac2: {div(rac1, rac2)}")
