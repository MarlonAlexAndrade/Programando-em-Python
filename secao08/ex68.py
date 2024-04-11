def intercalar(string01, string02):
    string_intercalada = []

    for char1, char2 in zip(string01, string02):
        string_intercalada.append(char1)
        string_intercalada.append(char2)
    
    if len(string01) > len(string02):
        string_intercalada.extend(string01[len(string02):])
    elif len(string02) > len(string01):
        string_intercalada.extend(string02[len(string01):])

    return ''.join(string_intercalada)

string01 = "Ola"
string02 = "Mundo"

print(intercalar(string01, string02))
