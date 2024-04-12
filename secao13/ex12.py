def contar_letras(texto):
    ocorrencias_letras = {}

    for caractere in texto:
        if caractere.isalpha():
            letra = caractere.lower()
            ocorrencias_letras[letra] = ocorrencias_letras.get(letra, 0) + 1
    
    return ocorrencias_letras


def calcular_estatisticas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

            num_caracteres = len(conteudo)
            num_linhas = conteudo.count('\n') + 1
            num_palavras = len(conteudo.split())

            ocorrencias_letras = contar_letras(conteudo)

            return num_caracteres, num_linhas, num_palavras, ocorrencias_letras
    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
        return None, None, None, None


def escrever_resultados(nome_arquivo_saida, num_caracteres, num_linhas, num_palavras, ocorrencias_letras):
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            arquivo_saida.write(f'Número de caracteres: {num_caracteres}\n')
            arquivo_saida.write(f'Número de linhas: {num_linhas}\n')
            arquivo_saida.write(f'Número de palavras: {num_palavras}\n')
            arquivo_saida.write('Ocorrências de cada letra no arquivo:\n')
            for letra, ocorrencias in ocorrencias_letras.items():
                arquivo_saida.write(f'{letra}: {ocorrencias}\n')


nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

num_caracteres, num_linhas, num_palavras, ocorrencias_letras = calcular_estatisticas_arquivo(nome_arquivo_entrada)

if num_caracteres is not None:
    escrever_resultados(nome_arquivo_saida, num_caracteres, num_linhas, num_palavras, ocorrencias_letras)
