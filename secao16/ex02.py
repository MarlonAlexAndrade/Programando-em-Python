class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura


class Agenda:
    def __init__(self):
        self.__pessoas = []

    def armazena_pessoa(self, pessoa):
        self.__pessoas.append(pessoa)

    def remove_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if pessoa.get_nome() == nome:
                self.__pessoas.remove(pessoa)
                return f"{nome} removido(a) da agenda."
        return f"{nome} não encontrado(a) na agenda."

    def busca_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if pessoa.get_nome() == nome:
                return pessoa
        return None

    def imprime_agenda(self):
        for pessoa in self.__pessoas:
            print(f"Nome: {pessoa.get_nome()}, Idade: {pessoa.get_idade()}, Altura: {pessoa.get_altura()}")

    def imprime_pessoa(self, index):
        if 0 <= index < len(self.__pessoas):
            pessoa = self.__pessoas[index]
            print(f"Nome: {pessoa.get_nome()}, Idade: {pessoa.get_idade()}, Altura: {pessoa.get_altura()}")
        else:
            print("Index out of range.")


pessoa1 = Pessoa("João", 30, 175)
pessoa2 = Pessoa("Maria", 25, 160)
pessoa3 = Pessoa("Pedro", 40, 180)

agenda = Agenda()
agenda.armazena_pessoa(pessoa1)
agenda.armazena_pessoa(pessoa2)
agenda.armazena_pessoa(pessoa3)

print("Agenda completa:")
agenda.imprime_agenda()
print()

print(agenda.remove_pessoa("Maria"))
print()

print("Agenda após a remoção:")
agenda.imprime_agenda()
print()

nome = "Pedro"
pessoa_encontrada = agenda.busca_pessoa(nome)
if pessoa_encontrada:
    print(f"{nome} encontrado na agenda.")
    print(f"Detalhes de {nome}:")
    print(f"Nome: {pessoa_encontrada.get_nome()}, Idade: {pessoa_encontrada.get_idade()}, Altura: {pessoa_encontrada.get_altura()}")
else:
    print(f"{nome} não encontrado na agenda.")
