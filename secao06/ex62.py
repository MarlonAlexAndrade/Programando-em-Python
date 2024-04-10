caracteres = 0

lista = ""
while lista != "sair":
    lista = input("Digite o numero por extenso: ")
    caracteres += len(lista)
    print("O tamanho da string é:", caracteres)
