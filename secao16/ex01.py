class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def imprimir(self):
        return f'O nome da pessoa é {self.__nome} sua idade é de {self.__idade} e tem {self.__altura} de altura'


pessoa01 = Pessoa('Joao', '34', '1.60')

print(pessoa01.imprimir())
