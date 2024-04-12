def contar_palavra_em_arquivo(nome_arquivo, palavra):
    contador = 0

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.lower()
            palavras_na_linha = linha.split()
            contador += palavras_na_linha.count(palavra.lower())
        
        return contador

nome_arquivo = input("Digite o nome do arquivo: ")
palavra = input("Digite a palavra que deseja contar: ")

ocorrencias = contar_palavra_em_arquivo(nome_arquivo, palavra)

if ocorrencias is not None:
    print(f'A palavra "{palavra}" aparece {ocorrencias} vezes no arquivo "{nome_arquivo}".')
