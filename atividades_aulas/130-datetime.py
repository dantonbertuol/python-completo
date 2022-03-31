from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

# Cria data instanciando
data = datetime(2019, 4, 20, 10, 53, 20) # Ano, Mes, Dia, Hora, Minuto, Segundo
print(data.strftime('%d/%m/%Y %H:%M:%S')) # Formata a data para DD/MM/YYYY HH:MM:SS

# Converter string para data
data = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data)

# Pegar o timestamp
print(data.timestamp())
# Converter timestamp para data
data = datetime.fromtimestamp(1555729200.0)
print(data)

# Timedelta é uma duração de tempo: exemplo 1 dia, 2 dias
data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data += timedelta(days=5, seconds=59)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# Calcula diferença entre datas
d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 20:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2-d1 # Time delta, quantidade absoluta de diferença
print(dif.total_seconds()) # Diferença em total de segundos
print(dif.days) # Diferença em dias

# Formatando datas em português
setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)
print(mes_atual, mdays[mes_atual])
