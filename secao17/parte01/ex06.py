class Retangulo:
    
    def __init__(self, comprimento, largura, area=None, perimetro=None):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        self.__area = self.__comprimento * self.__largura

    def calcular_perimetro(self):
        self.__perimetro =  (self.__comprimento * 2) + (self.__largura * 2)

    def imprimir(self):
        print(f'Comprimento: {self.__comprimento}')
        print(f'Largura: {self.__largura}')
        print(f'Area: {self.__area}')
        print(f'Perimetro: {self.__perimetro}')

retangulo01 = Retangulo(comprimento=4, largura=2)
retangulo01.calcular_area()
retangulo01.calcular_perimetro()
retangulo01.imprimir()
