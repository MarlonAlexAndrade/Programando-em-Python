multiplos = []
x = 0
i = 1

while x < 5:  
    if i % 3 == 0:
        multiplos.append(i)
        x += 1
    i += 1

for resultado in multiplos:
    print(resultado)