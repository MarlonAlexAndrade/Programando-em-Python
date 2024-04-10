nota01 = float(input("Digite a primeira nota: "))

nota02 = float(input("Digite a segunda nota: "))

nota03 = float(input("Digite a terceira nota: "))

media_ponderada = ((nota01 * 2)+ (nota02 * 3) + (nota03 * 5)) / 10

if media_ponderada >= 5:
    print(f'A sua media foi de {media_ponderada} você foi aprovado!')
elif media_ponderada >= 3:
    print(f'A sua media foi de {media_ponderada} você esta de recuperação!')
else:
    print(f'A sua media foi de {media_ponderada} você foi reprovado!')