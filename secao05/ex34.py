nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

if nota >= 0 and nota < 4:
    print("E")
elif nota < 5 and faltas <= 20:
    print("D")
elif nota < 5 and faltas > 20:
    print("E")
elif nota < 7.5 and faltas <= 20:
    print("C")
elif nota < 7.5 and faltas > 20:
    print("D")
elif nota < 9 and faltas <= 20:
    print("B")
elif nota < 9 and faltas > 20:
    print("C")
elif nota <= 10 and faltas <= 20:
    print("A")
elif nota <= 10 and faltas > 20:
    print("B")