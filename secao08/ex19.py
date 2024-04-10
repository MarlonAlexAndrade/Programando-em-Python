def maior_fator_primo(numero):
    maior_fator = 1
    
    while numero % 2 == 0:
        maior_fator = 2
        numero //= 2
    
    i = 3
    while i * i <= numero:
        while numero % i == 0:
            maior_fator = i
            numero //= i
        i += 2  
    
    
    if numero > 2:
        maior_fator = numero
    
    return maior_fator

numero = int(input("Digite um número inteiro positivo: "))

print("O maior fator primo de", numero, "é", maior_fator_primo(numero))
