import math


x = float(input('Введите значение координаты x: '))
y = float(input('Введите значение координаты y: '))

if y >= 0:
    if (y <= 2 and x <= 2 and x >= y - 2):
        print(True)
    else:
        print(False)
else:
    if (y >= -2 and x >= 0 and x <= y + 2):
        print(True)
    else:
        print(False)
