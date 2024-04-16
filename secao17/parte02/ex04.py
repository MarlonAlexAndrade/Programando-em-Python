class Equipamento:
    def __init__(self):
        self.__atributo1 = None
        self.__atributo2 = None


class Computador(Equipamento):
    def __init__(self, atributo1, atributo2):
        super().__init__()
        self.__atributo1 = atributo1
        self.__atributo2 = atributo2

    @property
    def atributo1(self):
        return self.__atributo1

    @atributo1.setter
    def atributo1(self, novo_valor):
        self.__atributo1 = novo_valor

    @property
    def atributo2(self):
        return self.__atributo2
    
    @atributo2.setter
    def atributo2(self, novo_valor):
        self.__atributo2 = novo_valor


computador1 = Computador("Processador Intel", "Memória RAM 8GB")

print(computador1.atributo1)  
print(computador1.atributo2)  
