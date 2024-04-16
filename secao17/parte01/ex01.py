class Pessoa:
    
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self, nome, endereco, telefone):
        print(f'O nome da pessoa é: {nome}')
        print(f'o endereco da pessoa é : {endereco}')
        print(f'O telefone é : {telefone}')


p1 = Pessoa('Marlon', 'Rua Bier', '4799135678')

