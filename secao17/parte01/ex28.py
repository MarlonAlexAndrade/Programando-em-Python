class Microondas:
    def __init__(self, ligado):
        self.__ligado = ligado

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False


microondas1 = Microondas(ligado=False)
microondas1.imprimir()
print()

print("Ligando o microondas...")
microondas1.ligar()
microondas1.imprimir()
print()

print("Desligando o microondas...")
microondas1.desligar()
microondas1.imprimir()
