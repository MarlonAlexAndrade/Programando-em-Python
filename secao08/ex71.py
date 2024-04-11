class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dentro_ret(v1, v2, p):
    if v1.x <= p.x <= v2.x and v1.y <= p.y <= v2.y:
        return True  
    else:
        return False  

v1 = Ponto(1, 1)  
v2 = Ponto(5, 5)  
p = Ponto(3, 3)   

resultado = dentro_ret(v1, v2, p)

if resultado:
    print(f"O ponto ({p.x}, {p.y}) está dentro do retângulo.")
else:
    print(f"O ponto ({p.x}, {p.y}) está fora do retângulo.")
