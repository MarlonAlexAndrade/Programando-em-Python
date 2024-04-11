def sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def anagrama(palavra01, palavra02):
    lista_palavra01 = list(palavra01)
    lista_palavra02 = list(palavra02)
    
    sort(lista_palavra01)
    sort(lista_palavra02)

    if lista_palavra01 == lista_palavra02:
        return "É um anagrama"
    else:
        return "Não é um anagrama"

palavra01 = "iracema"
palavra02 = "america"

print(f'As palavras {palavra01} e {palavra02}: {anagrama(palavra01, palavra02)}')
