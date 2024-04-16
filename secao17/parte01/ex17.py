class Eletrodomestico:
    def __init__(self, ligado):
        self.__ligado = ligado

    def imprimir(self):
        print(f'Ligado: {"Sim" if self.__ligado else "Não"}')


# Exemplo de uso do método construtor
eletrodomestico1 = Eletrodomestico(ligado=True)
eletrodomestico1.imprimir()
