nota01 = float(input("Digite a primeira nota: "))

nota02 = float(input("Digite a segunda nota: "))

nota03 = float(input("Digite a terceira nota: "))

media_ponderada = (nota01 + nota02 + (nota03 * 2)) / 4

if media_ponderada >= 60:
    print(f'A sua media foi de {media_ponderada} você foi aprovado!')
else:
    print(f'A sua media foi de {media_ponderada} você foi reprovado')