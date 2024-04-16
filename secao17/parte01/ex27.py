class Microondas:
    def __init__(self, ligado):
        self.__ligado = ligado

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')


microondas1 = Microondas(ligado=False)
microondas1.imprimir()
