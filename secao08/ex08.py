def hipotenusa(lado01, lado02):
    hipotenusa = (lado01**2 + lado02**2)**(1/2) 

    return hipotenusa

lado01 = int(input("Digite o valor do lado01: "))
lado02 = int(input("Digite o valor do lado02: "))

print(hipotenusa(lado01, lado02))
