def calculo_triangulo(lado01, lado02, lado03):
    if lado01 < lado02 + lado03 and lado02 < lado01 + lado03 and lado03 < lado01 + lado02:
        if lado01 == lado02 == lado03:
            return "O triangulo é um equilátero"
        elif lado01 == lado02 or lado02 == lado03 or lado03 == lado01:
            return "O triangulo é um isósceles"
        elif lado01 != lado02 != lado03:
            return "O triangulo é um escaleno"   
    else:
        return "Não é um triangulo"

    
lado01 = int(input("Digite o valor do lado lado01 do triangulo: "))
lado02 = int(input("Digite o valor do lado lado02 do triangulo: "))
lado03 = int(input("Digite o valor do lado lado03 do triangulo: "))

print(calculo_triangulo(lado01, lado02, lado03))
