import os

with open('arq.txt', 'w') as arquivo:
    while True:
        caracteres = input("Informe um carctere ou 0 para sair: ")
        if caracteres != '0':
            arquivo.write(caracteres)
            arquivo.write('\n')
        else:
            break

with open('arq.txt', 'r') as arquivo:
   with open('arq.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# Ou apenas 
# with open('arq.txt', 'r') as arquivo:
#     print(arquivo.read())
