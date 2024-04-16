class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha

    def imprimir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Marcha: {self.marcha}')


moto1 = Moto('Honda', 'CBR 600RR', 'Vermelha', 1)
moto1.imprimir()
