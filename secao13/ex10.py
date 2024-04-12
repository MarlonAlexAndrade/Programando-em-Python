nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

cidade_mais_populosa = None
habitantes_mais_populosos = 0

with open(nome_arquivo_entrada, 'r') as arquivo_entrada:

    for linha in arquivo_entrada:
        partes = linha.split()  
        nome_cidade = ' '.join(partes[:-1]) 
        habitantes = partes[-1]

        if habitantes.isdigit():
            num_habitantes = int(habitantes)

            if num_habitantes > habitantes_mais_populosos:
                cidade_mais_populosa = nome_cidade
                habitantes_mais_populosos = num_habitantes

if cidade_mais_populosa is not None:
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(f'Cidade mais populosa: {cidade_mais_populosa}, Habitantes: {habitantes_mais_populosos}')
    print("Arquivo de saída criado com sucesso.")
else:
    print("Não foi possível encontrar uma cidade mais populosa no arquivo de entrada.")
