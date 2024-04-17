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
# from csv import DictReader

# with open('lutadores.csv', encoding='utf-8') as arquivo:
#     leitor_csv = DictReader(arquivo, delimiter=',') # Dependendo do delimitador pode ser mudado
#     for linha in leitor_csv:
#         #Cada linha é um orderedDirect
#         print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
        

#Escrevendo arquivos CSV
# from csv import writer

# with open('filmes.csv', 'w') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Titutlo', 'Genero', 'Duração'])
#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o genero: ')
#             duracao = input('Informe a duração (em minutos): ')
#             escritor_csv.writerow([filme, genero, duracao])


# #DictWriter
# from csv import DictWriter

# with open('filmes3.csv', 'w') as arquivo:
#     cabecalho = ['Título', 'Gênero', 'Duração']
#     escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
#     escritor_csv.writeheader()
#     filme = None
#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o gênero: ')
#             duracao = input('Informe a duração (em minutos): ')
#             escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})


#Usado para transformar em binário ou converter novamente
#Tomar cuidado ao ler arquivos pickle desconhecidos, pode conter código malicioso

# import pickle

# class Animal:

#     def __init__(self, nome):
#         self.__nome = nome

#     @property
#     def nome(self):
#         return self.__nome

#     def comer(self):
#         print(f'{self.__nome} está comendo...')

# class Gato(Animal):
#     def __iniit__(self, nome):
#         super().__init__(nome)

#     def mia(self):
#         print(f'{self.nome} está miando...')

# class Cachorro(Animal):

#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def late(self):
#         print(f'{self.nome} está latindo...')

# felix = Gato('Felix')
# pluto = Cachorro('Pluto')


# with open('animais.pickle', 'wb') as arquivo:
#     pickle.dump((felix, pluto), arquivo)


#Fazer a leitura de dados em arquivos pickle

# with open('animais.pickle', 'rb') as arquivo:
#     gato, cachorro = pickle.load(arquivo)
#     print(f'O gato chama-se {gato.nome}')
#     gato.mia()
#     print(f'O tipo do gato é {type(gato)}')
#     print(f'O cachorro chama-se {cachorro.nome}')
#     cachorro.late()
#     print(f'O tipo de cachorro é {type(cachorro)}')


#JSON -> JavaScript Object Notation

# import json

# ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

# print(type(ret))

# print(ret)

# import jsonpickle

# class Gato:

#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca

#     @property
#     def nome(self):
#         return self.__nome
    
#     @property
#     def raca(self):
#         return self.__raca
    
# felix = Gato('Felix', 'Vira-Lata')

# print(felix.__dict__)

# ret = json.dumps(felix.__dict__)
# ret = jsonpickle.encode(felix)

# with open('felix.json', 'w') as arquivo:
#     ret = jsonpickle.encode(felix)
#     arquivo.write(ret)

# print(ret)


import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
