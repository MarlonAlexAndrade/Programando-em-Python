def escrever_arquivo_alunos(profissoes, anos):
    with open('empt.txt', 'w') as arquivo:
        for nome, ano in zip(profissoes, anos):
            nome_formatado = nome.ljust(40)  
            arquivo.write(f'{nome_formatado}{int(ano)} anos\n')


num_alunos = int(input("Digite o número de pessoas: "))

profissoes = []
anos = []

for i in range(num_alunos):
    nome = input(f"Digite o nome da profissão {i+1}: ")
    ano = float(input(f"Digite o tempo de serviço {i+1}: "))

    profissoes.append(nome)
    anos.append(ano)

escrever_arquivo_alunos(profissoes, anos)
