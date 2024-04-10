valor = float(input("Digite o valor total: "))

desconto = valor * 0.1

parcela = valor / 3

comissao = (valor - desconto) * 0.05

print(f'O valor a vista com desconto é de {valor - desconto}')
print(f'O valor parcelado em 3X é de R${parcela}')
print(f'A comissao do vendedor em caso de desconto é de R${comissao}')
print(f'A comissao do vendedor caso seja parcelada sera de R${valor * 0.05}')
