numero = int(input("Digite um numero: "))

i = 1

if numero > 0:
    for i in range(i, numero):
        if numero % i == 0:
            print(i)
else:
    print("Digite um numero valido!")