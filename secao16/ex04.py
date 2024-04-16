class Televisao:
    def __init__(self):
        self.__volume = 0
        self.__canal = 1

    def aumentar_volume(self):
        if self.__volume < 100:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def aumentar_canal(self):
        self.__canal += 1

    def diminuir_canal(self):
        if self.__canal > 1:
            self.__canal -= 1

    def trocar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.__canal = novo_canal

    @property
    def volume(self):
        return self.__volume

    @property
    def canal(self):
        return self.__canal


class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao

    def aumentar_volume(self):
        self.televisao.aumentar_volume()

    def diminuir_volume(self):
        self.televisao.diminuir_volume()

    def aumentar_canal(self):
        self.televisao.aumentar_canal()

    def diminuir_canal(self):
        self.televisao.diminuir_canal()

    def trocar_canal(self, novo_canal):
        self.televisao.trocar_canal(novo_canal)

    def consultar_volume(self):
        return self.televisao.volume

    def consultar_canal(self):
        return self.televisao.canal


tv = Televisao()
controle = ControleRemoto(tv)

controle.aumentar_volume()
controle.aumentar_volume()
print(f'Volume atual: {controle.consultar_volume()}')  

controle.diminuir_volume()
print(f'Volume atual: {controle.consultar_volume()}')  

controle.aumentar_canal()
controle.aumentar_canal()
print(f'Canal atual: {controle.consultar_canal()}')  

controle.diminuir_canal()
print(f'Canal atual: {controle.consultar_canal()}')  

controle.trocar_canal(7)
print(f'Canal atual: {controle.consultar_canal()}') 
