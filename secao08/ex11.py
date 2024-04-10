def calcular_media(nota01, nota02, nota03, letra):
    if letra == "A":
        media_aritmetica = (nota01 + nota02 + nota03) /3
        return media_aritmetica
    elif letra == "P":
        media_ponderada = (nota01 * 5 + nota02 * 3 + nota03 *2) / 10
        return media_ponderada
    else:
        return "Digite uma letra valida!"


nota01 = float(input("Digite a primera nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))
letra = input("Digite A maiusculo para calcular a media aritmetica ou P para a ponderada: ")

print(calcular_media(nota01, nota02, nota03, letra))
