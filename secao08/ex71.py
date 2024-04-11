def dentro_ret(v1, v2, p):
    if v1[0] <= p[0] <= v2[0] and v1[1] <= p[1] <= v2[1]:
        return True  
    else:
        return False  

v1 = (1, 1)
v2 = (5, 5)
p = (3, 3)

resultado = dentro_ret(v1, v2, p)

if resultado:
    print(f"O ponto ({p[0]}, {p[1]}) está dentro do retângulo.")
else:
    print(f"O ponto ({p[0]}, {p[1]}) está fora do retângulo.")
