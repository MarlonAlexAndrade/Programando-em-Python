preco = float(input("Digite o antigo preço do produto: "))


if preco <= 80:
    print(f'O novo preço é de {preco * 1.05}(Barato)')
elif preco > 80 and preco <= 120:
    print(f'O novo preço é de {preco * 1.10}(Normal)')
elif preco > 120 and preco <= 200:
    print(f'O novo preço é de {preco * 1.10}(Caro)')
elif preco > 200:
    print(f'O novo preço é de {preco * 1.10}(Muito Caro)')
