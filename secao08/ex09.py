def volume_cilindro(raio, altura):
    volume = 3.141592 * raio**2 * altura

    return volume

raio = float(input("Digite o valor do raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

print(volume_cilindro(raio, altura))