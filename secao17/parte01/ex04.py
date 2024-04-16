class Quadrado:
    def __init__(self, lado, area=None, perimetro=None):
        self.lado = lado
        self.area = area
        self.perimetro = perimetro

    def calcular_area(self):
        self.area = self.lado * self.lado

    def calcular_perimetro(self):
        self.perimetro = 4 * self.lado

    def imprimir(self):
        print("Lado:", self.lado)
        print("Área:", self.area)
        print("Perímetro:", self.perimetro)


quadrado = Quadrado(lado=5)
quadrado.calcular_area()
quadrado.calcular_perimetro()
quadrado.imprimir()
