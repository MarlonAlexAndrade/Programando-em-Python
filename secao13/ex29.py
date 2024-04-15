import os

def menu():
    print("\nMENU:")
    print("1. Criar o arquivo de dados")
    print("2. Incluir um determinado registro no arquivo")
    print("3. Excluir um determinado vendedor no arquivo")
    print("4. Alterar o valor de uma venda no arquivo")
    print("5. Imprimir os registros na saída padrão")
    print("6. Excluir o arquivo de dados")
    print("7. Finalizar o programa")
    return input("Escolha uma opção: ")

def criar_arquivo():
    with open("registros.txt", "w") as arquivo:
        arquivo.write("")

def incluir_registro():
    codigo = input("Digite o código do vendedor: ")
    nome = input("Digite o nome do vendedor: ")
    valor = input("Digite o valor da venda: ")
    mes = input("Digite o mês: ")

    with open("registros.txt", "a") as arquivo:
        arquivo.write(f"{codigo},{nome},{valor},{mes}\n")

def excluir_registro():
    codigo = input("Digite o código do vendedor a ser excluído: ")
    mes = input("Digite o mês do registro a ser excluído: ")

    with open("registros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("registros.txt", "w") as arquivo:
        for linha in linhas:
            campos = linha.strip().split(",")
            if campos[0] != codigo or campos[3] != mes:
                arquivo.write(linha)

def alterar_valor_venda():
    codigo = input("Digite o código do vendedor: ")
    mes = input("Digite o mês do registro: ")
    novo_valor = input("Digite o novo valor da venda: ")

    with open("registros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("registros.txt", "w") as arquivo:
        for linha in linhas:
            campos = linha.strip().split(",")
            if campos[0] == codigo and campos[3] == mes:
                campos[2] = novo_valor
                nova_linha = ",".join(campos) + "\n"
                arquivo.write(nova_linha)
            else:
                arquivo.write(linha)

def imprimir_registros():
    with open("registros.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())

def excluir_arquivo():  
    os.remove("registros.txt")


while True:
    opcao = menu()

    if opcao == '1':
        criar_arquivo()
    elif opcao == '2':
        incluir_registro()
    elif opcao == '3':
        excluir_registro()
    elif opcao == '4':
        alterar_valor_venda()
    elif opcao == '5':
        imprimir_registros()
    elif opcao == '6':
        excluir_arquivo()
    elif opcao == '7':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
