import math
mes = int(input('Введите номер места: '))
result = {True: math.ceil(mes / 4), False: 'Такого места нет'}[mes < 37]
print('Номер вашего купе:', result)
