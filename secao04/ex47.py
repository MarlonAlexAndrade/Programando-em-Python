numero = input("Digite um numero: ")

if int(numero) > 999 and int(numero) < 9999 :
    for i in range(4):
      print({numero[i]})
else:
   print("Digite um numero valido")