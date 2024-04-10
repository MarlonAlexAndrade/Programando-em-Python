quantidade_respostas = 10
quantidade_alunos = 5
quantidade_letras = 4

print("GABARITO")
print('-' * 40)
print("Digite as respostas das questões como A, B, C ou D.")
gabarito_respostas = []
for i in range(quantidade_respostas):
    resposta = input(f"Digite a resposta da questão {i + 1}: ").upper()
    while resposta not in ['A', 'B', 'C', 'D']:
        print("Por favor, digite uma resposta válida (A, B, C ou D).")
        resposta = input(f"Digite a resposta da questão {i + 1}: ").upper()
    gabarito_respostas.append(resposta)

print("RESPOSTAS DO GABARITO")
print('-' * 40)
print("[-]", end='')
for letra in range(quantidade_letras):
    print(f"[{chr(letra + 65)}]", end='')
print()
for i, resposta in enumerate(gabarito_respostas):
    print(f"[{i + 1}]", end='')
    for letra in range(quantidade_letras):
        print("[#]" if resposta == chr(letra + 65) else "[ ]", end='')
    print()

print("GABARITO DO ALUNO")
print('#' * 40)
gabarito_alunos = []
for i in range(quantidade_alunos):
    print(f"Digite as respostas do aluno [{i + 1}]:")
    gabarito_aluno = []
    for j in range(quantidade_respostas):
        resposta = input(f"Digite a resposta da questão {j + 1}: ").upper()
        while resposta not in ['A', 'B', 'C', 'D']:
            print("Por favor, digite uma resposta válida (A, B, C ou D).")
            resposta = input(f"Digite a resposta da questão {j + 1}: ").upper()
        gabarito_aluno.append(resposta)
    gabarito_alunos.append(gabarito_aluno)

print("ACERTOS DE CADA ALUNO")
print('-' * 40)
for i, aluno in enumerate(gabarito_alunos):
    pontuacao = sum(aluno[j] == gabarito_respostas[j] for j in range(quantidade_respostas))
    print(f"O aluno {i + 1} acertou {pontuacao} questões.")

input("Pressione Enter para encerrar o programa.")
