def ler_notas_alunos(nome_arquivo_entrada):
    alunos = []

    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        for linha in arquivo_entrada:
            partes = linha.split()  
            nome = ' '.join(partes[:40]) 
            notas = sorted(map(int, partes[40:]))
            alunos.append((nome, notas))

    return alunos

def escrever_notas_ordenadas(nome_arquivo_saida, alunos):
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        for aluno in alunos:
            notas_formatadas = ' '.join(map(str, aluno[1]))
            arquivo_saida.write(f"{aluno[0]} {notas_formatadas}\n")


nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

alunos = ler_notas_alunos(nome_arquivo_entrada)
alunos_ordenados = sorted(alunos, key=lambda x: x[1])

escrever_notas_ordenadas(nome_arquivo_saida, alunos_ordenados)
print(f"Dados dos alunos foram salvos no arquivo '{nome_arquivo_saida}'.")
