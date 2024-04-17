# Métodos de Data e Hora

# import datetime

# agora = datetime
# print(agora)
# print(type(agora))
# print(repr(agora))


# hoje = datetime.datetime.today()
# print(hoje)
# print(type(hoje))
# print(repr(hoje))

import datetime

# Encontrar o dia da semana weekday()

# Os dias da semana do método weekday() começa em 0,sendo esta a segunda-feira

# 0 - Segunda-Feira (Monday)
# 1 - Terça-Feira(Tuesday)
# 2 - Quarta-Feira (Wednesday)
# 3 - Quinta-Feira (Thursday)
# 4 -  Sexta-Feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)

# manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

# print(manutencao.weekday())

# import datetime

# aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

# aniversario = aniversario.split('/')

# aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

# if aniversario.weekday() == 0:
#     print('Você nasceu em uma segunda-feira')
# elif aniversario.weekday() == 1:
#     print('Você nasceu em uma terça-feira')
# elif aniversario.weekday() == 2:
#     print('Você nasceu em uma quarta-feira')
# elif aniversario.weekday() == 3:
#     print('Você nasceu em uma quinta-feira')
# elif aniversario.weekday() == 4:
#     print('Você nasceu em uma sexta-feira')
# elif aniversario.weekday() == 5:
#     print('Você nasceu no sabado')
# elif aniversario.weekday() == 6:
#     print('Você nasceu no domingo')

# import datetime
# # Formatando datas/horas com strftime() (String Format Time)
# # dd/mm/yyyy hora:minuto

# hoje = datetime.datetime.today()

# print(hoje)

# # '%d/%B/%Y' Passa o mes por escrito e b minusculo as primeiras iniciais

# hoje_formatado = hoje.strftime('%d/%m/%Y')

# print(hoje_formatado)

#Não funcionou
# Utilizando a biblioteca textblob
# import datetime
# from textblob import TextBlob

# def formata_data(data):
#     return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

# hoje = datetime.datetime.today()

# print(formata_data(hoje))

# import datetime

# nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

# print(nascimento)

# nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

# nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

# print(nascimento)


# Marcando o tempo de exeucação do nosso código com timeit
# import timeit

# Loop for
# tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# print(tempo)

# List Comprehension
# tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# print(tempo)

# Map
# tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# print(tempo)

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num  ** num +4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))

