def ler_dados(num_habitantes):
    habitantes = []
    for i in range(num_habitantes):
        sexo = input(f"Sexo do habitante F ou M {i+1}: ")
        cor_olhos = input(f"Cor dos olhos (A - Azuis ou C - Castanhos) do habitante {i+1}: ")
        cor_cabelos = input(f"Cor dos cabelos (L - Louros, P - Pretos ou C - Castanhos) do habitante {i+1}: ")
        idade = int(input(f"Idade do habitante {i+1}: "))
        habitante = (sexo, cor_olhos, cor_cabelos, idade)
        habitantes.append(habitante)
    return habitantes

def media_idade_olhos_castanhos_cabelos_pretos(habitantes):
    idades = [habitante[3] for habitante in habitantes if habitante[1] == 'C' and habitante[2] == 'P']
    if idades:
        return sum(idades) / len(idades)
    else:
        return 0

def maior_idade(habitantes):
    return max(habitante[3] for habitante in habitantes)

def quantidade_mulheres_jovens_olhos_azuis_cabelos_louros(habitantes):
    return sum(1 for habitante in habitantes if habitante[0] == 'F' and 18 <= habitante[3] <= 35
               and habitante[1] == 'A' and habitante[2] == 'L')


habitantes = ler_dados(5)
print("Média de idade das pessoas com olhos castanhos e cabelos pretos:", 
      media_idade_olhos_castanhos_cabelos_pretos(habitantes))
print("Maior idade entre os habitantes:", maior_idade(habitantes))
print("Quantidade de mulheres jovens com olhos azuis e cabelos louros:", 
      quantidade_mulheres_jovens_olhos_azuis_cabelos_louros(habitantes))
