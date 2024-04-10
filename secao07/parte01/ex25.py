vetor = []
i = 0
while len(vetor) != 100:
    i += 1
    if i % 7 != 0 and i % 1 != 7:
        vetor.append(i)
        
print(vetor)
