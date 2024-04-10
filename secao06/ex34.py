f = 1

while True:
    divisivel = True
    for j in range(1, 21):
        if f % j != 0:
            divisivel = False
            break

    if divisivel:
        print("O menor número divisível por todos os números de 1 a 10 é:", f)
        break

    f += 1
