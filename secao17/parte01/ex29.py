class Microondas:
    def __init__(self, ligado, porta_fechada):
        self.__ligado = ligado
        self.__porta_fechada = porta_fechada

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')
        print(f'Porta Fechada: {"Sim" if self.__porta_fechada else "Não"}')

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False


microondas1 = Microondas(ligado=False, porta_fechada=True)
microondas1.imprimir()
