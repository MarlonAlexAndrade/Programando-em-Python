def encontrar_maior_nota(nome_arquivo_entrada):
    maior_nota = 0
    aluno_com_maior_nota = None

    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        for linha in arquivo_entrada:
            partes = linha.split()  
            nome_aluno = ' '.join(partes[:-1]) 
            nota = float(partes[-1])

            if nota > maior_nota:
                aluno_com_maior_nota = nome_aluno
                maior_nota = nota

    return aluno_com_maior_nota, maior_nota

def escrever_resultado(nome_arquivo_saida, aluno_com_maior_nota, maior_nota):
    if aluno_com_maior_nota is not None:
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            arquivo_saida.write(f'Aluno com maior nota: {aluno_com_maior_nota}, Nota: {maior_nota}')
        print("Arquivo de saída criado com sucesso.")
    else:
        print("Não foi possível encontrar um aluno com maior nota no arquivo de entrada.")

nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

aluno_com_maior_nota, maior_nota = encontrar_maior_nota(nome_arquivo_entrada)
escrever_resultado(nome_arquivo_saida, aluno_com_maior_nota, maior_nota)
