import pickle

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

def salvar_alunos(nome_arquivo, alunos):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(alunos, arquivo)

def ler_alunos(nome_arquivo):
    with open(nome_arquivo, 'rb') as arquivo:
        alunos = pickle.load(arquivo)
    return alunos

def encontrar_maior_nota(alunos):
    maior_nota = 0
    nome_aluno_maior_nota = None

    for aluno in alunos:
        if aluno.nota > maior_nota:
            maior_nota = aluno.nota
            nome_aluno_maior_nota = aluno.nome

    return nome_aluno_maior_nota, maior_nota


num_alunos = int(input("Digite o número de alunos: "))

alunos = []
for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota final do aluno {i+1}: "))

    aluno = Aluno(nome[:40], nota)
    alunos.append(aluno)

nome_arquivo = input("Digite o nome do arquivo binário de saída: ")

salvar_alunos(nome_arquivo, alunos)
print(f"Dados dos alunos foram salvos no arquivo '{nome_arquivo}'.")

alunos_lidos = ler_alunos(nome_arquivo)
nome_aluno_maior_nota, maior_nota = encontrar_maior_nota(alunos_lidos)
print(f"Aluno com a maior nota: {nome_aluno_maior_nota}, Nota: {maior_nota}")

