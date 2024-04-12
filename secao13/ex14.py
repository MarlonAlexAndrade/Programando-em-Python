from datetime import datetime

def separar_nomes_datas(arquivo_entrada):
    dados = []
    with open(arquivo_entrada, 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            nome = ' '.join(partes[:-3])
            data = '/'.join(partes[-3:])
            dados.append((nome, data))
    return dados

def calcular_idade(data_nascimento, data_atual):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def escrever_resultado(arquivo_saida, dados):
    with open(arquivo_saida, 'w') as arquivo:
        for nome, data in dados:
            idade = calcular_idade(data, datetime.now())
            arquivo.write(f'{nome}: {idade} anos\n')

nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

dados = separar_nomes_datas(nome_arquivo_entrada)

if dados:
    escrever_resultado(nome_arquivo_saida, dados)
    print(f'Os resultados foram escritos no arquivo "{nome_arquivo_saida}" com sucesso.')
else:
    print(f'O arquivo "{nome_arquivo_entrada}" não contém dados válidos.')
