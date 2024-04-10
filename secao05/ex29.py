import random


acerto = 0
erro = 0
respostas_corretas = []

for _ in range(5):
    a = random.randrange(1,10)
    b = random.randrange(1,10)

    print(f' Qual é a soma de {a} + {b}')

    resposta = int(input("Digite a respota: "))   

    if a + b == resposta:
        acerto += 1
        respostas_corretas.append((a, b, resposta))
    else:
        erro += 1
    

print(f'Você teve {acerto} acertos e {erro} erros')
print("\nPerguntas e respostas corretas:")
for pergunta in respostas_corretas:
    print(f"A soma de {pergunta[0]} + {pergunta[1]} é {pergunta[2]}")
