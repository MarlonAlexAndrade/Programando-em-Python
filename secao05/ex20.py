a = int(input("Digite o valor do lado A do triangulo: "))
b = int(input("Digite o valor do lado B do triangulo: "))
c = int(input("Digite o valor do lado C do triangulo: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("O triangulo é um equilátero")
    elif a == b or b == c or c == a:
        print("O triangulo é um isósceles")
    elif a != b != c:
        print("O triangulo é um escaleno")   
else:
    print("Não é um triangulo")
    