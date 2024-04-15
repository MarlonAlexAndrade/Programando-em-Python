import pickle

def adicionar_contato(agenda, contato):
    agenda.append(contato)

def remover_contato(agenda, nome):
    for contato in agenda:
        if contato['nome'] == nome:
            agenda.remove(contato)
            return True
    return False

def pesquisar_contato(agenda, nome):
    for contato in agenda:
        if contato['nome'] == nome:
            return contato
    return None

def listar_contatos(agenda):
    for contato in agenda:
        print("Nome:", contato['nome'])
        print("Telefone:", contato['telefone'])
        print("Aniversário:", contato['dia_aniversario'], "/", contato['mes_aniversario'])

def listar_contatos_por_letra(agenda, letra):
    for contato in agenda:
        if contato['nome'].startswith(letra):
            print("Nome:", contato['nome'])
            print("Telefone:", contato['telefone'])
            print("Aniversário:", contato['dia_aniversario'], "/", contato['mes_aniversario'])

def imprimir_aniversariantes_do_mes(agenda, mes):
    for contato in agenda:
        if contato['mes_aniversario'] == mes:
            print("Nome:", contato['nome'])
            print("Telefone:", contato['telefone'])
            print("Aniversário:", contato['dia_aniversario'], "/", contato['mes_aniversario'])

def salvar_agenda(agenda):
    with open("agenda.pkl", "wb") as f:
        pickle.dump(agenda, f)

def carregar_agenda():
    try:
        with open("agenda.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def menu():
    print("AGENDA DE CONTATOS")
    print("Escolha uma opção:")
    print("(a) Inserir contato")
    print("(b) Remover contato")
    print("(c) Pesquisar contato pelo nome")
    print("(d) Listar todos os contatos")
    print("(e) Listar contatos por letra inicial")
    print("(f) Imprimir aniversariantes do mês")
    print("(s) Sair")

agenda = carregar_agenda()

while True:
    menu()
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "a":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        dia_aniversario = input("Dia do aniversário: ")
        mes_aniversario = input("Mês do aniversário: ")
        contato = {'nome': nome, 'telefone': telefone, 'dia_aniversario': dia_aniversario, 'mes_aniversario': mes_aniversario}
        adicionar_contato(agenda, contato)
        salvar_agenda(agenda)
        print("Contato adicionado com sucesso!")

    elif opcao == "b":
        nome = input("Digite o nome do contato a ser removido: ")
        if remover_contato(agenda, nome):
            salvar_agenda(agenda)
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "c":
        nome = input("Digite o nome do contato a ser pesquisado: ")
        contato = pesquisar_contato(agenda, nome)
        if contato:
            print("Contato encontrado:")
            print("Nome:", contato['nome'])
            print("Telefone:", contato['telefone'])
            print("Aniversário:", contato['dia_aniversario'], "/", contato['mes_aniversario'])
        else:
            print("Contato não encontrado.")

    elif opcao == "d":
        listar_contatos(agenda)

    elif opcao == "e":
        letra = input("Digite a letra inicial para listar os contatos: ")
        listar_contatos_por_letra(agenda, letra)

    elif opcao == "f":
        mes = input("Digite o número do mês para listar os aniversariantes: ")
        imprimir_aniversariantes_do_mes(agenda, mes)

    elif opcao == "s":
        salvar_agenda(agenda)
        print("Agenda salva. Encerrando programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
