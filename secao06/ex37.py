for i in range(1000, 9999):
    lista01 = []
    lista02 = []
    soma = 0
    
    lista01.append(i // 1 % 10)  
    lista01.append(i // 10 % 10) 
    lista02.append(i // 100 % 10)
    lista02.append(i // 1000 % 10)

    lista01.reverse()
    lista02.reverse()

    soma01 = int(''.join(map(str, lista01)))
    soma02 = int(''.join(map(str, lista02)))

    soma = (soma01 + soma02)

    if soma**2 == i:
        print(i)

