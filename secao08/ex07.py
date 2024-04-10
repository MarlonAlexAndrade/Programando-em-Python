def conversor_fahrenheit(celsius):
    fahrenheit = celsius *(9 / 5) + 32

    return fahrenheit


celsius = float(input("Digite a temperatura em celsius: "))

print(conversor_fahrenheit(celsius))