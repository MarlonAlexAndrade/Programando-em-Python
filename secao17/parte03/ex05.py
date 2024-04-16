class Pessoa:
    def __init__(self, codigo, nome, idade):
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


pessoa1 = Pessoa(1, "João", 30)
pessoa1.exibe()
print()
pessoa1.exibe_com_idade(0)  
