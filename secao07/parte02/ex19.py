matriz_notas = []

for i in range(2):
    matricula = int(input(f"Digite a matrícula do aluno {i+1}: "))
    media_provas = float(input(f"Digite a média das provas do aluno {i+1}: "))
    media_trabalhos = float(input(f"Digite a média dos trabalhos do aluno {i+1}: "))
    #Decidir se a nota vai precisar ser divida por 2
    nota_final = (media_provas + media_trabalhos)/2
    matriz_notas.append([matricula, media_provas, media_trabalhos, nota_final])

maior_nota_final = max(matriz_notas, key=lambda x: x[3])
matricula_maior_nota_final = maior_nota_final[0]

notas_finais = [aluno[3] for aluno in matriz_notas]
media_notas_finais = sum(notas_finais) / len(notas_finais)

print(f"\n Matrícula do aluno com a maior nota final: {matricula_maior_nota_final}")
print(f"Média aritmética das notas finais: {media_notas_finais:.2f}")
