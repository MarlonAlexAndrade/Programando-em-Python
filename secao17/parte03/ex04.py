class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def  exibe(self):
        print(f'Codigo: {self.__codigo}')
        print(f'Nome: {self.__nome}')
        print(f'Idade: {self.__idade}')

pessoa01 = Pessoa(1, 'Cadu', '16')

pessoa01.exibe()
