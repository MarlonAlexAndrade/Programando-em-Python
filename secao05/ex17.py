base_menor = int(input("Digite o valor da base menor do trapézio: "))

base_maior = int(input("Digite o valor da base maior do trapézio: "))

altura = int(input("Digite a altura do trapézio: "))

if base_menor > 0 and base_maior > 0:
    area_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f'A area do trapezio é de {area_trapezio}')
else:
    print("Digite um valor maior que zero!")