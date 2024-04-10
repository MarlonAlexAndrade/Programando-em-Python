altura = float(input("Digite a sua altura exemplo: 1.74: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura*altura)

if imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc < 25:
    print("Saudavel")
elif imc >= 25 and imc < 30:
    print("Peso em excesso")
elif imc >= 30 and imc < 35:
    print("Obesidade Grau l")
elif imc >= 35 and imc < 40:
    print("Obesidade Grau ll(Severa)")
elif imc <= 40:
    print("Obesidade Grau lll(Mórbida)")
