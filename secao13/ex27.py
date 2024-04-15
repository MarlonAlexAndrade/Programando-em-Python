def definir_turma():
    global turma
    turma = input("Informe o nome da turma: ")
    print("Informações da turma definidas com sucesso.")

def inserir_aluno_notas():
    global alunos_notas
    nome_aluno = input("Nome do aluno: ")
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou digite 'fim' para parar): ")
        if nota.lower() == 'fim':
            break
        notas.append(float(nota))
    alunos_notas[nome_aluno] = notas
    print("Notas do aluno inseridas com sucesso.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def exibir_alunos_medias():
    print("Alunos e médias:")
    for aluno, notas in alunos_notas.items():
        media = calcular_media(notas)
        print(f"Aluno: {aluno} - Média: {media:.2f}")

def exibir_alunos_aprovados():
    print("Alunos aprovados:")
    for aluno, notas in alunos_notas.items():
        media = calcular_media(notas)
        if media >= 7.0:
            print(f"Aluno: {aluno} - Média: {media:.2f}")

def exibir_alunos_reprovados():
    print("Alunos reprovados:")
    for aluno, notas in alunos_notas.items():
        media = calcular_media(notas)
        if media < 7.0:
            print(f"Aluno: {aluno} - Média: {media:.2f}")

def salvar_dados():
    with open("notas.txt", "w") as f:
        f.write("Turma: " + turma + "\n")
        for aluno, notas in alunos_notas.items():
            f.write(aluno + ": " + ", ".join(map(str, notas)) + "\n")
    print("Dados salvos em disco com sucesso.")


global alunos_notas
alunos_notas = {}
opcao = ''
while opcao != 'g':
    print("\nMENU:")
    print("(a) Definir informações da turma")
    print("(b) Inserir aluno e notas")
    print("(c) Exibir alunos e médias")
    print("(d) Exibir alunos aprovados")
    print("(e) Exibir alunos reprovados")
    print("(f) Salvar dados em Disco")
    print("(g) Sair do programa")
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'a':
        definir_turma()
    elif opcao == 'b':
        inserir_aluno_notas()
    elif opcao == 'c':
        exibir_alunos_medias()
    elif opcao == 'd':
        exibir_alunos_aprovados()
    elif opcao == 'e':
        exibir_alunos_reprovados()
    elif opcao == 'f':
        salvar_dados()
    elif opcao == 'g':
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
