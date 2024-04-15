def reverter_linha(linha):
    return linha[::-1]

def reverter_arquivo(entrada, saida):
    with open(entrada, 'r') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()

    linhas_revertidas = [reverter_linha(letras.strip()) for letras in linhas]

    with open(saida, 'w') as arquivo_saida:
        for letras in linhas_revertidas:
            arquivo_saida.write(letras + '\n')


arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
arquivo_saida = input("Digite o nome do arquivo de saída: ")
reverter_arquivo(arquivo_entrada, arquivo_saida)
print("Arquivo revertido com sucesso.")
