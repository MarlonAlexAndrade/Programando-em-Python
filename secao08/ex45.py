def desvio_padrao(vetor):
    media_vetor = sum(vetor) / len(vetor)
    soma_desvios_quadraticos = 0
    for valor in vetor:
        soma_desvios_quadraticos += (valor - media_vetor) ** 2
    desvio_padrao = (soma_desvios_quadraticos / len(vetor)) ** 0.5
    return desvio_padrao

vetor = [1, 2, 3, 4, 5]

print(f'Vetor: {vetor}')
print(f'Desvio padrão: {desvio_padrao(vetor)}')
