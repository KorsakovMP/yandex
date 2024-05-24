import math
import datetime
num_1 = int(input('Введи первое число: '))
num_2 = int(input('Введи второе число: '))
operation = ''
while operation not in ('+', '-', '*', '/', '//', '^'):
    operation = input(
        'Напиши, какую операцию ты хочешь выполнить (+, -, *, /, //(деление с остатком), ^(возведение в степень): '
    )
if operation == '+':
    print(num_1 + num_2)
if operation == '-':
    print(num_1 - num_2)
if operation == '*':
    print(num_1 * num_2)
if operation == '/':
    if num_2 == 0:
        print(f'{num_1}/{num_2} На ноль делить нельзя')
    else:
        print(num_1 / num_2)
if operation == '^':
    print(num_1 ** num_2)
if operation == '//':
    if num_2 == 0:
        print(f'{num_1}/{num_2} На ноль делить нельзя')
    else:
        print(f'Частное={num_1 // num_2} остаток={num_1 % num_2}')
