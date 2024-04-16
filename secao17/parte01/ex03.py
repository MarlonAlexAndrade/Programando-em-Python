class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return self.__lado * self.__lado
    
    def calcular_perimetro(self):
        return self.__lado * 4

    def imprimir(self):
        print(f'Lado: {self.__lado}')       
        print(f'Area: {self.__area}')
        print(f"Perímetro: {self.__perimetro}")


quadrado1 = Quadrado(lado=2)
quadrado1.imprimir() 
