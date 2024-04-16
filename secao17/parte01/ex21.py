class Televisor:
    def __init__(self, ligado, canal, volume):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')
        print(f'Canal: {self.__canal}')
        print(f'Volume: {self.__volume}')


televisor1 = Televisor(ligado=True, canal=5, volume=20)
televisor1.imprimir()
