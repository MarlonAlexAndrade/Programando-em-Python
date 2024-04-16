class Televisor:
    def __init__(self, ligado, canal, volume, numero_canais, volume_maximo):
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume
        self.__numero_canais = numero_canais
        self.__volume_maximo = volume_maximo

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')
        print(f'Canal: {self.__canal}')
        print(f'Volume: {self.__volume}')
        print(f'Número Máximo de Canais: {self.__numero_canais}')
        print(f'Volume Máximo: {self.__volume_maximo}')

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False


televisor1 = Televisor(ligado=False, canal=5, volume=20, numero_canais=100, volume_maximo=50)
televisor1.ligar()
televisor1.imprimir()

print("Desligando o televisor...")
televisor1.desligar()
televisor1.imprimir()
