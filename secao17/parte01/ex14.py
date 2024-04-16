class Moto:
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__menor_marcha = menor_marcha
        self.__maior_marcha = maior_marcha
        self.__ligada = ligada

    def imprimir(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Marcha: {self.__marcha}')
        print(f'Menor Marcha: {self.__menor_marcha}')
        print(f'Maior Marcha: {self.__maior_marcha}')
        print(f'Ligada: {"Sim" if self.__ligada else "Não"}')

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


moto1 = Moto(marca='Honda', modelo='CBR 600RR', cor='Vermelha', marcha=0, menor_marcha=0, maior_marcha=5, ligada=True)
moto1.imprimir()
