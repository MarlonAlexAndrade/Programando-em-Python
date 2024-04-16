class Elevador:
    
    def __init__(self, capacidade, total_andares):
        self.__andar_atual = 0
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presentes = 0

    def entra(self):
        if self.__pessoas_presentes < self.__capacidade:
            self.__pessoas_presentes += 1
        else:
            print("O elevador está cheio.")
            
    def sai(self):
        if self.__pessoas_presentes > 0:
            self.__pessoas_presentes -= 1
        else:
            print("O elevador está vazio.")

    def sobe(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print("O elevador já está no último andar.")

    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print("O elevador já está no térreo.")

    @property
    def andar_atual(self):
        return self.__andar_atual
    
    @andar_atual.setter
    def andar_atual(self, andar):
        self.__andar_atual = andar

    @property
    def total_andares(self):
        return self.__total_andares

    @total_andares.setter
    def total_andares(self, total_andares):
        self.__total_andares = total_andares

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def pessoas_presentes(self):
        return self.__pessoas_presentes
    
    @pessoas_presentes.setter
    def pessoas_presentes(self, pessoas_presentes):
        self.__pessoas_presentes = pessoas_presentes

    

meu_elevador = Elevador(capacidade=5, total_andares=10)

while True:
    print("\nEscolha uma ação:")
    print("1. Entrar no elevador")
    print("2. Sair do elevador")
    print("3. Subir um andar")
    print("4. Descer um andar")
    print("5. Sair do programa")

    escolha = input("Digite o número da ação desejada: ")

    if escolha == "1":
        meu_elevador.entra()
    elif escolha == "2":
        meu_elevador.sai()
    elif escolha == "3":
        meu_elevador.sobe()
    elif escolha == "4":
        meu_elevador.desce()
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, digite novamente.")

    print("\nEstado atual do elevador:")
    print(f'Andar atual: {meu_elevador.andar_atual}')
    print(f'Pessoas presentes: {meu_elevador.pessoas_presentes}')
