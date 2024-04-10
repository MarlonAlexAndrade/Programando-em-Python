resistencia = 1

while resistencia != 0:
    resistor01 = int(input("Digite o valor do primeiro resistor: "))
    resistor02 = int(input("Digite o valor do segundo resistor: "))

    resistencia = (resistor01 * resistor02) / (resistor01 + resistor02)

    print(f'A resistencia é de {resistencia}')