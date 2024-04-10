import statistics

list = [12, 24, 36, 48, 60]

desvio = statistics.pstdev(list)

print(f'O desvio inicial da lista é {desvio}')
