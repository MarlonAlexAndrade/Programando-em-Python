class Pessoa:
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf


class Cliente(Pessoa):

    def __init__ (self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
