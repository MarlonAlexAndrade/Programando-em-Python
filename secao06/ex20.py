numero = 0
par = 0
contador = 0

while numero != 1000:
    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        print(f'O numero {numero} é par')
        par += 1
    else:
        print(f'O numero {numero} não é par')       
    contador += 1
    
print(f'A quantidade de numeros pares lidos é de {par} e a de dados lidos é de {contador}')
