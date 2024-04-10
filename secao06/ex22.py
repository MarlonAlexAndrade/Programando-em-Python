ativo = True
contador = 1
soma = 0

while ativo == True:
    nota = float(input("Digite uma nota: "))
    if nota >= 0 and nota <= 10:
        soma += nota 
        media = soma / contador

        print(f'A media é de {media}')
        contador += 1
    else:
        ativo = False
        