altura_chico = 1.5
altura_ze = 1.1
anos = 0

while altura_ze < altura_chico:
    anos += 1

    altura_chico += 0.02 
    altura_ze += 0.03 
 
print(f'Serão nescessarios {anos} anos para ze passar chico e ele tera {altura_ze} e chico tera {altura_chico}')