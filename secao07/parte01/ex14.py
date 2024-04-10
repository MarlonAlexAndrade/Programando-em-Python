lista = [1, 2, 3, 4, 4, 5, 5, 8, 8, 1]
duplicados = []
unicos = []

for i in lista:
        if i in unicos:
            duplicados.append(i)
        else:
            unicos.append(i)
            
print(duplicados)