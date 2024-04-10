def criar_vetor(numero):
    return [int(digito) for digito in str(numero)][::-1]  


def somar_vetores(vetor1, vetor2):
    tamanho = max(len(vetor1), len(vetor2))  
    resultado = [0] * (tamanho + 1)  

    for i in range(tamanho):
        soma = resultado[i] 
        if i < len(vetor1):
            soma += vetor1[i]  
        if i < len(vetor2):
            soma += vetor2[i]  

        resultado[i] = soma % 10  
        resultado[i + 1] = soma // 10  

    return resultado[::-1] if resultado[-1] == 0 else resultado 


a = int(input("Digite o primeiro número (positivo, menor que 10000): "))
b = int(input("Digite o segundo número (positivo, menor que 10000): "))

vetor_a = criar_vetor(a)
vetor_b = criar_vetor(b)

vetor_soma = somar_vetores(vetor_a, vetor_b)

print(f'Vetor soma: {vetor_soma}')
