class Moto:
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__menor_marcha = menor_marcha
        self.__maior_marcha = maior_marcha

    def imprimir(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Marcha: {self.__marcha}')
        print(f'Menor Marcha: {self.__menor_marcha}')
        print(f'Maior Marcha: {self.__maior_marcha}')

    def marcha_acima(self):
        if self.__marcha < self.__maior_marcha:
            self.__marcha += 1
        else:
            print(f'A marcha {self.__marcha} é o máximo.')

    def marcha_abaixo(self):
        if self.__marcha > self.__menor_marcha:
            self.__marcha -= 1
        else:
            print(f'A marcha {self.__marcha} é o limite mínimo.')


moto1 = Moto('Honda', 'CBR 600RR', 'Vermelha', 1, 0, 5) 
moto1.marcha_abaixo()  
moto1.marcha_abaixo()  
moto1.marcha_acima()  
moto1.marcha_acima()  
moto1.marcha_acima()  
moto1.marcha_acima()  
moto1.marcha_acima() 
moto1.marcha_acima() 
moto1.imprimir()
