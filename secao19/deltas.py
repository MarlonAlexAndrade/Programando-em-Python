# import datetime

# data_hoje = datetime.datetime.now()

# aniversario = datetime.datetime(2025, 3, 3, 0)

# tempo_para_evento = aniversario - data_hoje

# print(type(tempo_para_evento))

# print(repr(tempo_para_evento))

# print(tempo_para_evento)

# print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas... ')

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)

