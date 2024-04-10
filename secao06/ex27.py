numero = int(input("Digite um numero inteiro: "))

x = 1

if numero <= 0:
    print("O valor de n deve ser um número inteiro e positivo.")
else:
    harmonica = 0
    for i in range(1, numero + 1):
        harmonica += x / i
        x +=1
        
    print(f'O valor de H(n) é: {harmonica}')
