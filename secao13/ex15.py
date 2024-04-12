from datetime import datetime

def calcular_idade(ano_nascimento, ano_corrente):
    idade = ano_corrente - ano_nascimento
    if idade < 18:
        return "menor de idade"
    elif idade > 18:
        return "maior de idade"
    else:
        return "entrando na maior idade"

def processar_arquivo(nome_arquivo_entrada, nome_arquivo_saida, ano_corrente):
        with open(nome_arquivo_entrada, 'r') as arquivo_entrada, open(nome_arquivo_saida, 'w') as arquivo_saida:
            for linha in arquivo_entrada:
                nome, ano_nascimento = linha.strip().split()
                ano_nascimento = int(ano_nascimento)
                idade = calcular_idade(ano_nascimento, ano_corrente)
                arquivo_saida.write(f'{nome.ljust(40)}: {idade}\n')
        print(f'O arquivo "{nome_arquivo_saida}" foi gerado com sucesso.')

ano_corrente = int(input("Digite o ano corrente: "))
nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

processar_arquivo(nome_arquivo_entrada, nome_arquivo_saida, ano_corrente)
