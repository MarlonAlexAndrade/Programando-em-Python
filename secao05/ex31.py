altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

if altura < 1.2:
    if peso < 60:
        print("A")
    elif peso >= 60 and peso<= 90:
        print("D")
    elif peso > 90:
        print("G")
elif altura >= 1.2 and altura <= 1.7:
    if peso < 60:
        print("B")
    elif peso >= 60 and peso <= 90:
        print("E")
    elif peso > 90:
        print("H")
elif altura > 1.7:
    if peso < 60:
        print("C")
    elif peso >= 60 and peso<= 90:
        print("F")
    elif peso > 90:
        print("I")
