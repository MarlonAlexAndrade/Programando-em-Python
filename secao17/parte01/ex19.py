class Eletrodomestico:
    def __init__(self, ligado):
        self.__ligado = ligado

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')

    def liga_desliga(self):
        if self.__ligado == True:
            self.__ligado = False
        elif self.__ligado == False:
            self.__ligado = True


eletrodomestico1 = Eletrodomestico(ligado=True)
eletrodomestico1.liga_desliga()
eletrodomestico1.imprimir()
