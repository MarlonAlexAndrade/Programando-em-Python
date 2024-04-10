num = float(input("Digite um numero: "))

if num > 0:
    quadrado = num **2
    print(f'O numero {num} ao quadrado é {quadrado}')
    
    raiz = num ** 0.5
    print(f'A raiz quadrada do numero {num} é {raiz}')
    
else:
    print("O numero é invalido!")