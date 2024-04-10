n = int(input("Digite o numero de numeros impares: "))
i = 0
x = 2

while i < n:
    if x % 2 != 0:
        print(x)
        i += 1
    x += 1
