quantidade_questoes = 10
quantidade_alunos = 3
quantidade_letras = 5  

print("GABARITO")
print('-' * 40)
print("Digite as respostas das questões como A, B, C, D ou E.")
gabarito_respostas = []
for i in range(quantidade_questoes):
    resposta = input(f"Digite a resposta da questão {i + 1}: ").upper()
    while resposta not in ['A', 'B', 'C', 'D', 'E']:
        print("Por favor, digite uma resposta válida (A, B, C, D ou E).")
        resposta = input(f"Digite a resposta da questão {i + 1}: ").upper()
    gabarito_respostas.append(resposta)

print("\nGABARITO DO ALUNO")
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

print("\nGABARITO DOS ALUNOS")
print('#' * 40)
alunos = []
for i in range(quantidade_alunos):
    matricula = int(input(f"Digite a matrícula do aluno {i + 1}: "))
    respostas_aluno = []
    for j in range(quantidade_questoes):
        resposta = input(f"Digite a resposta do aluno {i + 1} na questão {j + 1}: ").upper()
        while resposta not in ['A', 'B', 'C', 'D', 'E']:
            print("Por favor, digite uma resposta válida (A, B, C, D ou E).")
            resposta = input(f"Digite a resposta do aluno {i + 1} na questão {j + 1}: ").upper()
        respostas_aluno.append(resposta)
    alunos.append((matricula, respostas_aluno))

print("\nNOTAS DOS ALUNOS")
print('-' * 40)
total_aprovados = 0
for aluno in alunos:
    matricula, respostas_aluno = aluno
    nota = sum(respostas_aluno[j] == gabarito_respostas[j] for j in range(quantidade_questoes))
    percentual_aprovacao = (nota / quantidade_questoes) * 100
    print(f"Matrícula: {matricula}")
    print(f"Respostas: {respostas_aluno}")
    print(f"Nota: {nota}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
    if percentual_aprovacao >= 70:
        total_aprovados += 1

percentual_total_aprovacao = (total_aprovados / quantidade_alunos) * 100
print("\nRESUMO")
print('-' * 40)
print(f"Total de alunos aprovados: {total_aprovados}/{quantidade_alunos}")
print(f"Percentual de aprovação total: {percentual_total_aprovacao:.2f}%")
