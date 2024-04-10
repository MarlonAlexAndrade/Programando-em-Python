idade = int(input("Digite a sua idade: "))

tempo_servico = int(input("Digite o seu tempo de serviço: "))

if idade >= 65 or tempo_servico >= 30:
    print("Podera se aposentar!")
elif idade >= 60 and tempo_servico >= 25:
    print("Podera se aposentar!")
else:
    print("Não podera se aposentar")
