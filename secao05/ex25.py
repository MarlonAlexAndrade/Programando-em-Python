import math

def calcula_raizes(a, b, c):
    if a == 0:
        return "Não é uma equação de segundo grau."
    else:
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            return "Não existe raiz real."
        elif discriminante == 0:
            raiz = -b / (2*a)
            return "Raiz única:", raiz
        else:
            raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
            raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
            return "Raízes:", raiz1, raiz2

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

raizes = calcula_raizes(a, b, c)

print(f'As raízes da equação são: {raizes}')
