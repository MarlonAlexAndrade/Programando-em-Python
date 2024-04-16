class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def imprimir(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Marcha: {self.__marcha}')

    def marcha_acima(self):
        if self.__marcha < 5:
            self.__marcha += 1
        
    def marcha_abaixo(self):
        if self.__marcha > 0:
            self.__marcha -= 1

moto1 = Moto('Honda', 'CBR 600RR', 'Vermelha', 1)
moto1.marcha_acima()
moto1.marcha_acima()
moto1.imprimir()
