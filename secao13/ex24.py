import pickle

def entrada_produto(despensa):
    codigo = input("Digite o código do produto: ")
    descricao = input("Digite a descrição do produto: ")
    quantidade = int(input("Digite a quantidade a ser adicionada: "))
    if codigo in despensa:
        despensa[codigo] += quantidade
    else:
        despensa[codigo] = quantidade
    print("Produto adicionado com sucesso.")

def retirada_produto(despensa):
    codigo = input("Digite o código do produto: ")
    if codigo in despensa:
        quantidade = int(input("Digite a quantidade a ser retirada: "))
        if quantidade <= despensa[codigo]:
            despensa[codigo] -= quantidade
            print("Retirada realizada com sucesso.")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado.")

def relatorio_geral(despensa):
    print("Relatório Geral:")
    for codigo, quantidade in despensa.items():
        print(f"Código: {codigo}, Quantidade: {quantidade}")

def relatorio_indisponiveis(despensa):
    print("Produtos Indisponíveis:")
    for codigo, quantidade in despensa.items():
        if quantidade == 0:
            print(f"Código: {codigo}")

def salvar_despensa(despensa, arquivo):
    with open(arquivo, 'wb') as f:
        pickle.dump(despensa, f)

def carregar_despensa(arquivo):
    try:
        with open(arquivo, 'rb') as f:
            despensa = pickle.load(f)
    except FileNotFoundError:
        despensa = {}
    return despensa

def menu():
    print("\n1. Adicionar Produto")
    print("2. Retirar Produto")
    print("3. Relatório Geral")
    print("4. Relatório de Produtos Indisponíveis")
    print("5. Sair")


arquivo = 'despensa.bin'
despensa = carregar_despensa(arquivo)

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        entrada_produto(despensa)
    elif opcao == '2':
        retirada_produto(despensa)
    elif opcao == '3':
        relatorio_geral(despensa)
    elif opcao == '4':
        relatorio_indisponiveis(despensa)
    elif opcao == '5':
        salvar_despensa(despensa, arquivo)
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

