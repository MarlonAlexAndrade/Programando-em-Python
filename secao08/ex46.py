def imprimir_normal(vetor):
    print("Impressão normal do vetor:")
    for elemento in vetor:
        print(elemento, end=" ")
    print()  

def imprimir_inversa(vetor):
    print("Impressão inversa do vetor:")
    vetor_inverso = vetor[::-1]
    return vetor_inverso

def media_aritmetica(vetor):
    return sum(vetor) / len(vetor)

vetor = [1, 2, 3, 4, 5]
imprimir_normal(vetor)
print(imprimir_inversa(vetor))
print("Média aritmética:", media_aritmetica(vetor))
