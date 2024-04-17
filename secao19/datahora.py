# import datetime

# # print(dir(datetime))

# print(datetime.datetime.now())

# # replace() para fazer ajustes na data/hora
# inicio = datetime.datetime.now()

# print(inicio)

# # Alterar o horario
# inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

# print(type(evento))
# print(type('31/12/2018'))


# print(evento)

# nascimento = input('Informa sua data de nascimento(dd/mm/yyyy): ')

# print(nascimento)

# nascimento = nascimento.split('/')

# nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

# print(nascimento)

# print(type(nascimento))

import datetime

evento = datetime.datetime(2019, 1, 1, 0)

#Acesso individual dos elemtnos de data e hora

print(evento.year)
print(evento.month)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(evento)