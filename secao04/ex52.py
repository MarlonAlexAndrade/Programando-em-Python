aposta01 = int(input("Digite o apostado pela primeira pessoa: "))

aposta02 = int(input("Digite o apostado pela segunda pessoa: "))

aposta03 = int(input("Digite o apostado pela terceira pessoa: "))

valor_premio = int(input("Digite o valor do premio: "))

resultado = valor_premio / (aposta01 + aposta02 + aposta03)

aposta01 = resultado * aposta01
aposta02 = resultado * aposta02
aposta03 = resultado * aposta03

print(f'O premio de {valor_premio} sera de {aposta01} para a primeira pessoa, {aposta02} para a segunda e {aposta03} para a terceira')

