def formatar_letras(texto):
    texto_modificado = ''
    for letra in texto:
            texto_modificado += letra.lower()
            
    return texto_modificado

nome_arquivo01 = input("Digite o nome do arquivo de entrada: ")

with open(nome_arquivo01, 'r', encoding='utf-8') as arquivo_entrada:
    conteudo_original = arquivo_entrada.read()

    conteudo_modificado = formatar_letras(conteudo_original)

    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo_modificado)

    print("Arquivo de saída criado com sucesso.")
