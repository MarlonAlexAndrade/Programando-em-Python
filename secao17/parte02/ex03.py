class Equipamento:
    def __init__(self):
        self.__atributo1 = None
        self.__atributo2 = None


class Computador(Equipamento):
    def __init__(self, atributo1, atributo2):
        super().__init__()  
        self.__atributo1 = atributo1
        self.__atributo2 = atributo2
