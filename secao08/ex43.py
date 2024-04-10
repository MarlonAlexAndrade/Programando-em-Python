import random

def preencher_vetor_aleatorio(tamanho):
    vetor = []


    while len(vetor) < tamanho:
        numero = random.randint(1, 20)  
        if numero not in vetor:  
            vetor.append(numero)  
    
    return vetor

tamanho = int(input('Digite o tamanho do vetor: '))
vetor = preencher_vetor_aleatorio(tamanho)

print(f'Vetor preenchido aleatoriamente sem repetição: {vetor}')
