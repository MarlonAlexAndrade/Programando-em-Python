class Pessoa:
    def __init__(self, codigo=None, nome=None, idade=None):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def exibe(self):
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        print("Idade:", self.idade)

    def exibe_com_idade(self, mostrar_idade=1):
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        if mostrar_idade == 1:
            print("Idade:", self.idade)

    def __init__(self):
        print("Construtor padrão")


class TestaPessoa:
    def main(self):
        pessoa = Pessoa()


testador = TestaPessoa()
testador.main()
