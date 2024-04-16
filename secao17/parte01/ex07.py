class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return  3.141516  * self.__raio * self.__raio 
    
    def calcular_perimetro(self):
        return 2 * 3.141516 * self.__raio
    
    def imprimir(self):
        print(f'Raio: {self.__raio}')
        print(f'Area: {self.__area}')
        print(f'Perimetro: {self.__perimetro}')

circulo01 = Circulo(raio = 10)
circulo01.imprimir()
