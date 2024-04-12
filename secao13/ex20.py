def escrever_arquivo_alunos(nome_arquivo, nomes, notas):
    with open(nome_arquivo, 'w') as arquivo:
        for nome, nota in zip(nomes, notas):
            nome_formatado = nome.ljust(40)  
            arquivo.write(f"{nome_formatado}{nota}\n")


num_alunos = int(input("Digite o número de alunos: "))

nomes = []
notas = []

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota final do aluno {i+1}: "))

    nomes.append(nome)
    notas.append(nota)

nome_arquivo = input("Digite o nome do arquivo de saída: ")

escrever_arquivo_alunos(nome_arquivo, nomes, notas)
print(f"Dados dos alunos foram salvos no arquivo '{nome_arquivo}'.")
