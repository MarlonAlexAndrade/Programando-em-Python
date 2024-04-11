class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def soma(v1, v2):
    res_x = v1.x + v2.x
    res_y = v1.y + v2.y
    res_z = v1.z + v2.z
    return Vetor(res_x, res_y, res_z)

v1 = Vetor(1.0, 2.0, 3.0)
v2 = Vetor(4.0, 5.0, 6.0)

resultado = soma(v1, v2)

print(f"Resultado da soma: ({resultado.x}, {resultado.y}, {resultado.z})")
