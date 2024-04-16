class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

class Agenda:
    def __init__(self):
        self.__pessoas = []

    def armazena_pessoa(self, nome, idade, altura):
        pessoa = Pessoa(nome, idade, altura)
        self.__pessoas.append(pessoa)

    def remove_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if pessoa._Pessoa__nome == nome:  
                self.__pessoas.remove(pessoa)
                return f"{nome} removido(a) da agenda."
        return f"{nome} não encontrado(a) na agenda."

    def busca_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if pessoa._Pessoa__nome == nome:  
                return pessoa
        return None

    def imprime_agenda(self):
        for pessoa in self.__pessoas:
            print(f"Nome: {pessoa._Pessoa__nome}, Idade: {pessoa._Pessoa__idade}, Altura: {pessoa._Pessoa__altura}")

    def imprime_pessoa(self, index):
        if 0 <= index < len(self.__pessoas):
            pessoa = self.__pessoas[index]
            print(f"Nome: {pessoa._Pessoa__nome}, Idade: {pessoa._Pessoa__idade}, Altura: {pessoa._Pessoa__altura}")
        else:
            print("Index out of range.")


pessoa1 = Pessoa("João", 30, 175)
pessoa2 = Pessoa("Maria", 25, 160)
pessoa3 = Pessoa("Pedro", 40, 180)

agenda = Agenda()
agenda.armazena_pessoa(pessoa1._Pessoa__nome, pessoa1._Pessoa__idade, pessoa1._Pessoa__altura)
agenda.armazena_pessoa(pessoa2._Pessoa__nome, pessoa2._Pessoa__idade, pessoa2._Pessoa__altura)
agenda.armazena_pessoa(pessoa3._Pessoa__nome, pessoa3._Pessoa__idade, pessoa3._Pessoa__altura)

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
    print(f"Nome: {pessoa_encontrada._Pessoa__nome}, Idade: {pessoa_encontrada._Pessoa__idade}, Altura: {pessoa_encontrada._Pessoa__altura}")
else:
    print(f"{nome} não encontrado na agenda.")
