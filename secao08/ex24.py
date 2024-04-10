def triangulo(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

altura = int(input('Digite a altura do triângulo (n): '))
triangulo(altura)

