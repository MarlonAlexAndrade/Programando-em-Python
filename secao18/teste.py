#  Não funcinou
# with open('lutadores.csv') as arquivo:
#     dados = arquivo.read()
#     dados = dados.split(',')[2:]
#     print(dados)

#Reader
# from csv import reader
# with open('lutadores.csv', encoding='utf-8') as arquivo:
#     leitor_csv = reader(arquivo)
#     next(leitor_csv) # Pular o cabeçalho
#     for linha in leitor_csv:
#         #Cada linha é uma lista
#         print(f'{linha[0]} nasceu em {linha[1]} e {linha[2]} centimetros')

#DictReader
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # Dependendo do delimitador pode ser mudado
    for linha in leitor_csv:
        #Cada linha é um orderedDirect
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
        