class Televisor:
    def __init__(self, ligado, canal, volume):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')
        print(f'Canal: {self.__canal}')
        print(f'Volume: {self.__volume}')

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False


# Exemplo de uso dos métodos ligar e desligar
televisor1 = Televisor(ligado=False, canal=5, volume=20)
televisor1.ligar()
televisor1.imprimir()

print("Desligando o televisor...")
televisor1.desligar()
televisor1.imprimir()
