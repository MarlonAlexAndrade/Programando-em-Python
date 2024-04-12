def substituir_vogais_por_asterisco(texto):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    texto_modificado = ''
    for letra in texto:
        if letra in vogais:
            texto_modificado += '*'
        else:
            texto_modificado += letra
    return texto_modificado

nome_arquivo = input("Digite o nome do arquivo de entrada: ")

with open(nome_arquivo, 'r') as arquivo_entrada:
    conteudo_original = arquivo_entrada.read()

    conteudo_modificado = substituir_vogais_por_asterisco(conteudo_original)

    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo_modificado)

    print("Arquivo de saída criado com sucesso.")


