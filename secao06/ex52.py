def calcular_notas(saque):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = {}

    for nota in notas:
        quantidade = saque // nota
        saque %= nota
        quantidade_notas[nota] = quantidade

    return quantidade_notas


saque = int(input("Digite o valor do saque: "))

notas = calcular_notas(saque)

print("Quantidade de notas necessárias para o saque:")
for nota, quantidade in notas.items():
    print(f"{quantidade} nota(s) de {nota}")
