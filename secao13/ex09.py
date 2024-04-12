nome_arquivo01 = input("Digite o nome do primeiro arquivo de entrada: ")
nome_arquivo02 = input("Digite o nome do segundo arquivo de entrada: ")

with open(nome_arquivo01, 'r', encoding='utf-8') as arquivo01, open(nome_arquivo02, 'r', encoding='utf-8') as arquivo02:
    conteudo01 = arquivo01.read()
    conteudo02 = arquivo02.read()

conteudo_concatenado = conteudo01 + "\n" + conteudo02

nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(conteudo_concatenado)

print("Arquivo de saída criado com sucesso.")
