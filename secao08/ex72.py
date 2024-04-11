def soma(v1, v2):
    res_x = v1[0] + v2[0]
    res_y = v1[1] + v2[1]
    res_z = v1[2] + v2[2]
    return (res_x, res_y, res_z)

v1 = (1.0, 2.0, 3.0)
v2 = (4.0, 5.0, 6.0)

resultado = soma(v1, v2)

print(f"Resultado da soma: {resultado}")
