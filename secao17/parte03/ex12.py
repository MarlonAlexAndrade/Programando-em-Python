class Pessoa:
    def __init__(self, codigo=None, nome=None, idade=None):
        print("Construtor padrão")
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def exibe(self, mostrar_idade=True):
        print("Informações da Pessoa:")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        if mostrar_idade:
            print(f"Idade: {self.idade}")


class TestaPessoa:
    def __init__(self):
        print("Instanciando objeto usando o construtor padrão")
        self.pessoa = Pessoa()

    def testar_exibe_sem_parametro(self):
        print("\nTestando exibe() sem parâmetro")
        self.pessoa.codigo = 123
        self.pessoa.nome = "Fulano"
        self.pessoa.idade = 30
        self.pessoa.exibe()

    def testar_exibe_com_parametro_1(self):
        print("\nTestando exibe() com parâmetro 1")
        self.pessoa.codigo = 456
        self.pessoa.nome = "Ciclano"
        self.pessoa.idade = 25
        self.pessoa.exibe(1)

    def testar_exibe_com_parametro_diferente_de_1(self):
        print("\nTestando exibe() com parâmetro diferente de 1")
        self.pessoa.codigo = 789
        self.pessoa.nome = "Beltrano"
        self.pessoa.idade = 35
        self.pessoa.exibe(False)


# Teste da classe TestaPessoa
teste = TestaPessoa()
teste.testar_exibe_sem_parametro()
teste.testar_exibe_com_parametro_1()
teste.testar_exibe_com_parametro_diferente_de_1()
