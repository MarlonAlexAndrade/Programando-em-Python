class Aluno:
    def __init__(self, matricula, sobrenome, ano_nascimento):
        self.matricula = matricula
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

def cadastrar_alunos(numero_alunos):
    alunos = []
    for i in range(numero_alunos):
        print(f"Informações do aluno {i+1}:")
        matricula = input("Matrícula: ")
        sobrenome = input("Sobrenome: ")
        ano_nascimento = input("Ano de nascimento: ")
        aluno = Aluno(matricula, sobrenome, ano_nascimento)
        alunos.append(aluno)
    return alunos

def gravar_em_arquivo(alunos):
    with open("alunos.txt", "w") as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno.matricula}, {aluno.sobrenome}, {aluno.ano_nascimento}\n")


numero_alunos = int(input("Informe o número de alunos a serem cadastrados: "))
alunos = cadastrar_alunos(numero_alunos)
gravar_em_arquivo(alunos)
print("Cadastro de alunos concluído e gravado no arquivo alunos.txt")
