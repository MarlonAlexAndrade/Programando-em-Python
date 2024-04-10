notas_alunos = []

for i in range(10):
    valor = []
    for j in range(3):
        nota = float(input(f"Digite a nota do aluno {i+1} na prova {j+1}: "))
        valor.append(nota)
    notas_alunos.append(valor)

piores_provas = []
for aluno in notas_alunos:
    pior_prova = aluno.index(min(aluno))  
    piores_provas.append(pior_prova)

pior_prova1 = piores_provas.count(0)
pior_prova2 = piores_provas.count(1)
pior_prova3 = piores_provas.count(2)

print(f"Número de alunos cuja pior nota foi na prova 1: {pior_prova1}")
print(f"Número de alunos cuja pior nota foi na prova 2: {pior_prova2}")
print(f"Número de alunos cuja pior nota foi na prova 3: {pior_prova3}")
