import math
mes = int(input('введите номер места:'))
if mes<37:
    k=math.ceil(mes / 4)
    print('номер вашего купе:', k)
else:
    print('Такого места нет')
