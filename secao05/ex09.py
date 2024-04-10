salario = float(input("Digite o salario: "))

prestacao = float(input("Digite o valor da prestação: "))

porcentagem = (20 * salario) / 100 

if prestacao > porcentagem:
    print("Emprestimo não concedido!")
else: 
    print("Emprestimo concedido!")