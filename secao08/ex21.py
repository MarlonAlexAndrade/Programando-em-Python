def numeros_primos(numero):
    primos = []
    for i in range(2, numero + 1):
        eh_primo = True
        for j in range(2, i):
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    return primos

numero = int(input("Digite o número final: "))

print(numeros_primos(numero))
