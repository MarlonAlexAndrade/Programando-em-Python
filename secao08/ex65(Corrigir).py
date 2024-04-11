def concatenar(str1, str2, N):
    str_concatenada = str1[:]  
    max_letras = min(N, len(str2))

    str_concatenada.extend(str2[:max_letras])  
    return ''.join(str_concatenada)

str1 = ['H', 'e', 'l', 'l', 'o', ',', ' ']  
str2 = ['w', 'o', 'r', 'l', 'd', '!']     
N = 2

print(f'String concatenada: {concatenar(str1, str2, N)}')
