class Circulo:
    def __init__(self, raio, area = None, perimetro = None):
        self.__raio = raio
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        self.__area =  3.141516  * self.__raio * self.__raio 
    
    def calcular_perimetro(self):
        self.__perimetro  = 2 * 3.141516 * self.__raio
    
    def imprimir(self):
        print(f'Raio: {self.__raio}')
        print(f'Area: {self.__area}')
        print(f'Perimetro: {self.__perimetro}')

circulo01 = Circulo(raio = 10)
circulo01.calcular_area()
circulo01.calcular_perimetro()
circulo01.imprimir()
