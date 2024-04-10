maior_palindromo = 0

for i in range(100, 999):
    for x in range(100, 999):
        produto = i * x
        
        if str(produto) == str(produto)[::-1]:
            if produto > maior_palindromo:
                maior_palindromo = produto

print(f'O maior palíndromo é: {maior_palindromo}')
