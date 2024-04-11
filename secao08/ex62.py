def tamanho(str, strsize):
    size = 0  
    while size < len(str) and str[size] != '\0':
        size += 1   
    
    strsize[0] = size
    return size  

string = "Anagrama!"  
tamanho_da_string = [0]  


print(f'O comprimento da string é: {tamanho(string, tamanho_da_string)}')
