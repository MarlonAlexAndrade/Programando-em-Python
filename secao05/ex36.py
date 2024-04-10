valor_venda = float(input("Digite o valor da venda: "))

if valor_venda >= 100000:
    print(f'O valor da comissão fica em {700 + (valor_venda * 0.16)}')
elif valor_venda < 100000 and valor_venda >= 80000:
    print(f'O valor da comissão fica em {650 + (valor_venda * 0.14)}')
elif valor_venda < 80000 and valor_venda >= 60000:
    print(f'O valor da comissão fica em {600 + (valor_venda * 0.14)}')
elif valor_venda < 60000 and valor_venda >= 40000:
    print(f'O valor da comissão fica em {550 + (valor_venda * 0.14)}')
elif valor_venda < 40000 and valor_venda>= 20000:
    print(f'O valor da comissão fica em {500 + (valor_venda * 0.14)}')
elif valor_venda < 20000:
    print(f'O valor da comissão fica em {400 + (valor_venda * 0.14)}')
