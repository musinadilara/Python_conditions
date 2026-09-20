import math


a = float(input('Введите значение переменной a: '))
b = float(input('Введите значение переменной b: '))
x = float(input('Введите значение переменной x: '))

if 3 * a > b:
    y = math.log(x**2) - math.exp(x / 3)
else:
     y = math.atan(2 * x - 0.6)
print('Значение y для заданных a, b и x:', y)

