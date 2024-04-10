sexo = input("Digite o seu sexo M masuclino e F femenino: ")

altura = float(input("Digite a sua altura: "))


if sexo == "M":
   peso_ideal = (72.7 * altura) -58
   print(f'O seu peso ideal é de {peso_ideal}')
else:
   peso_ideal = (62.1 * altura) -44.7
   print(f'O seu peso ideal é de {peso_ideal}')
   