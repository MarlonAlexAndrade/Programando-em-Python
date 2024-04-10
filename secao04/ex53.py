comprimento = float(input("Digite o comprimennto do terreno: "))

largura = float(input("Digite a largura do terreno: "))

preco_tela = float(input("Digite o preco do metro de tela: "))

perimetro = comprimento + comprimento + largura + largura

preco = perimetro * preco_tela

print(f'O preco para cercar o terreno com tela é de {preco}')