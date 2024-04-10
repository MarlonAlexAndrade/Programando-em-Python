import random

numero = random.randint(1, 10)
acerto = 0
contador = 0
while acerto != numero:
    jogada = int(input("Digite um numero: "))

    contador += 1

    if jogada <= 0 or jogada > 1000:
        print("Digite um numero valido!")
    elif jogada > numero:
        print("Seu chute é maior que o numero: ")
    elif jogada < numero:
        print("Seu chute é menor que o numero: ")
    else:
        print(f'Você acertou o numero é {numero}, você levou {contador} jogadas')
        acerto = numero