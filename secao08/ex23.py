def triangulo(n):
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)


altura = int(input('Digite a altura do triângulo (n): '))
triangulo(altura)
