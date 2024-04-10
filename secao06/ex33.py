multiplos = int(input("Digite um numero inteiro: "))
i = 2
j = 3
x = 1

while multiplos > 0:
    if x % i == 0 or x % j == 0:  
        print(x)
        multiplos -= 1

    x += 1  
