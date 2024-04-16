class Pessoa:
    
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        print(f'O nome da pessoa é: {self.__nome}')
        print(f'O endereco é: {self.__endereco}')
        print(f'O telefone é: {self.__telefone}')


p1 = Pessoa('Marlon', 'Rua Bier', '4799135678')

p1.imprimir()
