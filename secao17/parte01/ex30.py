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

    def fecharPorta(self):
        self.__porta_fechada = True

    def abrirPorta(self):
        self.__porta_fechada = False


microondas1 = Microondas(ligado=False, porta_fechada=False)
microondas1.imprimir()
print()

print("Fechando a porta do microondas...")
microondas1.fecharPorta()
microondas1.imprimir()
print()

print("Abrindo a porta do microondas...")
microondas1.abrirPorta()
microondas1.imprimir()
