class Equipamento:
    def __init__(self):
        self.__atributo1 = None
        self.__atributo2 = None


class Computador(Equipamento):
    def __init__(self, atributo1, atributo2, atributo_herdado1, atributo_herdado2):
        super().__init__()
        self.__atributo1 = atributo1
        self.__atributo2 = atributo2
        self.__atributo_herdado1 = atributo_herdado1
        self.__atributo_herdado2 = atributo_herdado2

    @property
    def atributo_herdado1(self):
        return self.__atributo_herdado1

    @atributo_herdado1.setter
    def atributo_herdado1(self, novo_valor):
        self.__atributo_herdado1 = novo_valor

    @property
    def atributo_herdado2(self):
        return self.__atributo_herdado2
    
    @atributo_herdado2.setter
    def atributo_herdado2(self, novo_valor):
        self.__atributo_herdado2 = novo_valor


class TestaEquipamento:

    @staticmethod
    def main():
        equipamento = Equipamento()
        equipamento._Equipamento__atributo1 = "Atributo 1 Equipamento"
        equipamento._Equipamento__atributo2 = "Atributo 2 Equipamento"

        computador = Computador("Atributo 1 Computador", "Atributo 2 Computador",
                                "Atributo Herdado 1 Equipamento", "Atributo Herdado 2 Equipamento")

        print("Atributos do Equipamento:")
        print(f"Atributo 1: {equipamento._Equipamento__atributo1}")
        print(f"Atributo 2: {equipamento._Equipamento__atributo2}")

        print("\nAtributos do Computador:")
        print(f"Atributo 1: {computador._Computador__atributo1}")
        print(f"Atributo 2: {computador._Computador__atributo2}")
        print(f"Atributo Herdado 1: {computador._Computador__atributo_herdado1}")
        print(f"Atributo Herdado 2: {computador._Computador__atributo_herdado2}")


TestaEquipamento.main()
