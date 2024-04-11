def ler_string(vetor, tamanho):
    i = 0
    while i < tamanho:
        caractere = input("Digite um caractere (ou pressione Enter para finalizar): ")
        if caractere == '':  
            break
        vetor[i] = caractere
        i += 1
    return i  

tamanho_maximo = 10
vetor = [''] * tamanho_maximo  

quantidade_caracteres_lidos = ler_string(vetor, tamanho_maximo)

print("String lida:", ''.join(vetor[:quantidade_caracteres_lidos]))
