sair = True

while sair == True:
    velocidade = int(input("Digite a velocidade: "))

    print("1- Caso desejar converter km/h para m/s.")
    print("2- Caso desejar converter m/s para km/h.")
    print("3- Caso desejar sair.")

    opcao = int(input("Opção: "))

    if opcao == 1:
        velocidade /=  3.6
        print(f'A velocidade é de {velocidade} ms/s')
    elif opcao == 2:
        velocidade *= 3.6
        print(f'A velocidade é de {velocidade} km/h')
    else:
        sair = False