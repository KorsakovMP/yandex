# def check_day(day):
#     if day == 'сб'or day ==  'вс':
#         return 'Выходной'
#     else:
#         return 'Будний'
#
#
# print(check_day(day=input()))

# def allow_to_go(high, day):
#     if day == 'сб'or day ==  'вс':
#         return True
#     else:
#         if high > 2.5:
#             return False
#         return True
#
#
# print(allow_to_go(float(input()),input()))


# def perim_and_square(a, b, unit_of_measurement):
#     return f'{2 * (a + b)} {unit_of_measurement}', f'{a * b} кв. {unit_of_measurement} '
#
#
# print(
#     *perim_and_square(
#         a=int(input()),
#         b=int(input()),
#         unit_of_measurement=input(),
#     ),
#     sep='\n'
# )

# def convert_units(number, unit_of_measurement, unit_of_measurement2):
#     distance_convert_value = {
#         'м': 1,
#         'мм': 0.001,
#         'см': 0.01,
#         'км': 1000,
#     }
#     return number * distance_convert_value[unit_of_measurement] / distance_convert_value[unit_of_measurement2]
#
# print(convert_units(number=int(input()), unit_of_measurement=input(), unit_of_measurement2=input()))

# def convert_units(number, unit_of_measurement):
#     distance_convert_value = {
#         'м': 1,
#         'мм': 0.001,
#         'см': 0.01,
#         'км': 1000,
#     }
#     number_m = number * distance_convert_value[unit_of_measurement]
#     number_sm = number_m / distance_convert_value['см']
#     number_mm = number_m / distance_convert_value['мм']
#     if unit_of_measurement == 'мм':
#         return f'{number_mm} мм = {number_sm} см = {number_m} м'
#     elif unit_of_measurement == 'см':
#         return f'{number_sm} см = {number_mm} мм = {number_m} м'
#     elif unit_of_measurement == 'м':
#         return f'{number_m} м = {number_mm} мм = {number_sm} см'
#
#
# assert convert_units(number=10, unit_of_measurement='мм') == '10.0 мм = 1.0 см = 0.01 м'
# assert convert_units(number=256, unit_of_measurement='мм') == '256.0 мм = 25.6 см = 0.256 м'
#
# print(
#     convert_units(
#         number=int(input()),
#         unit_of_measurement=input(),
#     )
# )
# def normaliz(n):
#     if n % 1 == 0:
#         return int(n)
#     return n
#
#
# def calculate_square(a, b, unit_of_measurement):
#     distance_convert_value = {
#         'м': 1,
#         'мм': 0.001,
#         'см': 0.01,
#         'км': 1000,
#     }
#     a_m = a * distance_convert_value[unit_of_measurement]
#     a_sm = a_m / distance_convert_value['см']
#     a_mm = a_m / distance_convert_value['мм']
#     b_m = b * distance_convert_value[unit_of_measurement]
#     b_sm = b_m / distance_convert_value['см']
#     b_mm = b_m / distance_convert_value['мм']
#     square_m = a_m * b_m
#     square_mm = a_mm * b_mm
#     square_sm = a_sm * b_sm
#     if unit_of_measurement == 'мм':
#         return f'Площадь = {normaliz(square_mm)} кв. мм = {normaliz(square_sm)} кв. см = {normaliz(square_m)} кв. м'
#     elif unit_of_measurement == 'см':
#         return f'Площадь = {normaliz(square_sm)} кв. см = {normaliz(square_mm)} кв. мм = {normaliz(square_m)} кв. м'
#     elif unit_of_measurement == 'м':
#         return f'Площадь = {normaliz(square_m)} кв. м = {normaliz(square_mm)} кв. мм = {normaliz(square_sm)} кв. см'
#
#
# print(calculate_square(a=int(input()), b=int(input()), unit_of_measurement=input()))
# assert calculate_square(a=1, b=3, unit_of_measurement='мм') == 'Площадь = 3 кв. мм = 0.03 кв. см = 3e-06 кв. м'
# assert calculate_square(a=2, b=4, unit_of_measurement='см') == 'Площадь = 8 кв. см = 800 кв. мм = 0.0008 кв. м'
# assert calculate_square(a=3, b=5, unit_of_measurement='м') == 'Площадь = 15 кв. м = 15000000 кв. мм = 150000 кв. см'

# def factorial(n):
#     if n <= 2:
#         return n
#     return factorial(n - 1) * n

# def factorial(n):
#     value = 1
#     for i in range(1, n + 1):
#         value *= i
#     return value
#
# print(factorial(n=int(input())))
# assert factorial(n=3) == 6
# assert factorial(n=4) == 24

# def factorial(n):
#     value = 1
#     for i in range(1, n + 1):
#         value *= i
#     return value
#
#
# def binom(n, k):
#     return int((factorial(n=n)) / (factorial(n=k) * factorial(n=n-k)))
#
#
# print(binom(n=int(input()), k=int(input())))
# assert binom(n=10, k=1) == 10
# assert binom(n=11, k=2) == 55

# def calculate_currency(money_rub: int, exchange_rate: float):
#     return money_rub * exchange_rate
#
#
# print(calculate_currency(int(input()), float(input())))
# assert calculate_currency(10, 70.5) == 705.0
# assert calculate_currency(21, 71.6) == 1503.6

# def calculate_currency(money_rub: int, exchange_rate_usd: float, exchange_rate_eur: float):
#     return money_rub / exchange_rate_usd, money_rub / exchange_rate_eur
#
#
# print(
#     *calculate_currency(
#         int(input()),
#         float(input()),
#         float(input())
#     ), sep='\n'
# )
# assert calculate_currency(100, 70.5, 75.0) == (1.4184397163120568, 1.3333333333333333)
# assert calculate_currency(2100, 71.6, 76.1) == (29.329608938547487, 27.595269382391592)

# DIGITS = {
#     0: '',
#     1: 'один',
#     2: 'два',
#     3: 'три',
#     4: 'четыре',
#     5: 'пять',
#     6: 'шесть',
#     7: 'семь',
#     8: 'восемь',
#     9: 'девять',
# }
#
# TENS = {
#     1: 'десять',
#     2: 'двадцать',
#     3: 'тридцать',
#     4: 'сорок',
#     5: 'пятьдесят',
#     6: 'шестьдесят',
#     7: 'семьдесят',
#     8: 'восемьдесят',
#     9: 'девяносто',
# }
#
# TEENS = {
#     10: 'десять',
#     11: 'одиннадцать',
#     12: 'двенадцать',
#     13: 'тринадцать',
#     14: 'четырнадцать',
#     15: 'пятнадцать',
#     16: 'шестнадцать',
#     17: 'семнадцать',
#     18: 'восемнадцать',
#     19: 'девятнадцать'
# }
#
#
# def num_to_words(num):
#     # if num >= 1 and num <= 9:
#     if 1 <= num <= 9:
#         return DIGITS[num]
#     elif 10 <= num <= 19:
#         return TEENS[num]
#     elif 20 <= num <= 99:
#         n1 = num // 10
#         n0 = num % 10
#         return f'{TENS[n1]} {DIGITS[n0]}'
#
# # print(num_to_words(int(input())))
# assert num_to_words(2) == 'два'
# assert num_to_words(1) == 'один'
# assert num_to_words(10) == 'десять'
# assert num_to_words(11) == 'одиннадцать'
# assert num_to_words(19) == 'девятнадцать'
# assert num_to_words(99) == 'девяносто девять'
# assert num_to_words(37) == 'тридцать семь'

# def correct_len(proposal):
#     count = 0
#     for symbol in proposal:
#         if symbol not in (' ', '\n'):
#             count += 1
#
#     if 500 <= count <= 1000:
#         return True
#     return False
#
#
# # print(correct_len(input()))
# assert correct_len(
#     'Работа или учёба? Тут вроде бы всё очевидно: в школу идут поучиться, на стажировку — поработать. Это верно, но лишь отчасти. Стажёры в Прогрессе тоже постоянно учатся: знакомятся со внутренними инструментами, осваивают промышленное программирование, изучают наши сервисы с изнанки. Студенты школ, в свою очередь, работают. Под лекции, семинары и практикумы у них отведена первая часть программы, а после неё — работа над проектом в команде с другими слушателями. Разница в том, что стажёры учатся прямо во время рабочего процесса, а студенты школ сначала интенсивно занимаются, а потом применяют полученные знания на практике.') == True
# assert correct_len(
#     'Раньше студенты школ делали учебные проекты — сами для себя, чтобы закрепить навыки. Сейчас и на стажировке и в школах большинство задач реальные. Написанный код имеет все шансы стать частью одного из сервисов Прогресса, и результаты труда увидят не только коллеги и менторы, но и пользователи.') == False
#
# def count_different_symbols(proposal):
#     count = 0
#     count_alfa = 0
#     count_digit = 0
#     for synbol in proposal:
#         if synbol.isalpha():
#             count_alfa += 1
#         elif synbol.isdigit():
#             count_digit += 1
#         else:
#             count += 1
#     return f'Количество алфавитных символов: {count_alfa}\nКоличество цифровых символов: {count_digit}\nКоличество других символов: {count}'
#
#
# print(count_different_symbols(input()))
# assert count_different_symbols(
#     'Проверка: 55555') == 'Количество алфавитных символов: 8\nКоличество цифровых символов: 5\nКоличество других символов: 2'
# assert count_different_symbols(
#     'Проверка: 12345') == 'Количество алфавитных символов: 8\nКоличество цифровых символов: 5\nКоличество других символов: 2'
# assert count_different_symbols(
#     'С Новым 2023-м Годом! Ура!') == 'Количество алфавитных символов: 15\nКоличество цифровых символов: 4\nКоличество других символов: 7'

# def say_good_time(time):
#     if 0 <= time <= 5 or time in [0, 23]:
#         return 'Доброй ночи!'
#     elif 6 <= time <= 11:
#         return 'Доброе утро!'
#     elif 12<= time <= 17:
#         return 'Добрый день!'
#     else:
#         return 'Добрый вечер!'
#
# print(say_good_time(time=int(input())))
# assert say_good_time(0) == 'Доброй ночи!'
# assert say_good_time(10) == 'Доброе утро!'

# def say_good_time(time):
#     if 0 <= time <= 5 or time in [0, 23]:
#         return 'Доброй ночи!'
#     elif 6 <= time <= 11:
#         return 'Доброе утро!'
#     elif 12 <= time <= 17:
#         return 'Добрый день!'
#     else:
#         return 'Добрый вечер!'
#
# for i in range(24):
#     print(f'На часах {i}:00')
#     print(say_good_time(time=i))