def troque(valor01, valor02):
    lista = [valor01, valor02]
    lista_inversa = lista[::-1]

    return lista_inversa

valor01 = input("Digite um valor: ")
valor02 = input("Digite um segundo valor: ")

print(troque(valor01, valor02))
