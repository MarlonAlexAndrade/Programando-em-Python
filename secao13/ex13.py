def criar_lista_contatos():
    lista_contatos = {}
    while True:
        nome = input("Digite um nome : ")
        telefone = int(input("Digite um número de telefone (ou 0 para sair): "))
        if telefone == 0:
            break
        lista_contatos[nome] = telefone
    return lista_contatos


def escrever_resultados(nome_arquivo_saida, lista_contatos):
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            for nome, telefone in lista_contatos.items():
                arquivo_saida.write(f'{nome}: {telefone}\n')

nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

lista_contatos = criar_lista_contatos()

if lista_contatos:
    escrever_resultados(nome_arquivo_saida, lista_contatos)
