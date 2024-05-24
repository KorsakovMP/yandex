# def hello(name='Роб'):
#     print('Привет,', name)
#
# hello(name='мир')

# def Rob_helps(subject=''):
#     print('Привет! Меня зовут Роб.\n'
#           'Я стажёр в компании «Прогресс».\n'
#           'Знаю основы программирования на Python.\n\n'
#           'Могу рассказать про три функции:\n'
#           '1. print()\n'
#           '2. input()\n'
#           '3. int()')
#
#
# Rob_helps()

# def Rob_helps(subject=''):
#     text = {'print': ('Функция print() используется в Python для вывода данных на экран. Внутри круглых '
#                       'скобок мы пишем, что хотим напечатать. Если это текст, то обязательно '
#                       'указываем его внутри одинарных или двойных кавычек.'),
#             '': ('Привет! Меня зовут Роб.\n'
#                    'Я стажёр в компании «Прогресс».\n'
#                    'Знаю основы программирования на Python.\n\n'
#                    'Могу рассказать про три функции:\n'
#                    '1. print()\n'
#                    '2. input()\n'
#                    '3. int()')
#             }
#
#     print(text.get(subject))
#
#
# Rob_helps()
# print()
# Rob_helps('print')

# def Rob_helps(subject=''):
#     text = {'print': ('Функция print() используется в Python для вывода данных на экран. Внутри круглых '
#                       'скобок мы пишем, что хотим напечатать. Если это текст, то обязательно '
#                       'указываем его внутри одинарных или двойных кавычек.'),
#             'input': ('Функция input() используется в Python для считывания данных. Она всегда пишется с круглыми '
#                       'скобками. Когда программа доходит до места, где есть input(), она ждёт, пока пользователь '
#                       'введёт текст с клавиатуры (ввод завершается нажатием клавиши Enter). Введённая строка '
#                       'подставляется на место input().'),
#             '': ('Привет! Меня зовут Роб.\n'
#                  'Я стажёр в компании «Прогресс».\n'
#                  'Знаю основы программирования на Python.\n\n'
#                  'Могу рассказать про три функции:\n'
#                  '1. print()\n'
#                  '2. input()\n'
#                  '3. int()')
#             }
#
#     print(text.get(subject))
#
#
# Rob_helps()
# print()
# Rob_helps('print')
# print()
# Rob_helps('input')


# def Rob_helps(subject=''):
#     text = {'print': ('Функция print() используется в Python для вывода данных на экран. Внутри круглых '
#                       'скобок мы пишем, что хотим напечатать. Если это текст, то обязательно '
#                       'указываем его внутри одинарных или двойных кавычек.'),
#             'input': ('Функция input() используется в Python для считывания данных. Она всегда пишется с круглыми '
#                       'скобками. Когда программа доходит до места, где есть input(), она ждёт, пока пользователь '
#                       'введёт текст с клавиатуры (ввод завершается нажатием клавиши Enter). Введённая строка '
#                       'подставляется на место input().'),
#             'int': ('Функция int() используется в Python для преобразования строки к целому числу. Буквально int() '
#                     'означает следующее: «Возьми то, что указано в качестве аргумента в скобках, и преврати это в '
#                     'целое число».'),
#             '': ('Привет! Меня зовут Роб.\n'
#                  'Я стажёр в компании «Прогресс».\n'
#                  'Знаю основы программирования на Python.\n\n'
#                  'Могу рассказать про три функции:\n'
#                  '1. print()\n'
#                  '2. input()\n'
#                  '3. int()')
#             }
#
#     print(text.get(subject, 'У меня пока нет описания этой команды.'))
#     # try:
#     #     print(text[subject])
#     # except KeyError:
#     #     print('У меня пока нет описания этой команды.')
#
# Rob_helps()
# print()
# Rob_helps('print')
# print()
# Rob_helps('input')
# print()
# Rob_helps('int')
# print()
# Rob_helps('другое')

# def Rob_helps(subject='', example=False):
#     subject_text = {
#         '':'Привет! Меня зовут Роб.\nЯ стажёр в компании «Прогресс».\nЗнаю основы программирования на Python.\n\nМогу рассказать про три функции:\n1. print()\n2. input()\n3. int()\n\nФункция print() используется в Python для вывода данных на экран. Внутри круглых скобок мы пишем, что хотим напечатать. Если это текст, то обязательно указываем его внутри одинарных или двойных кавычек.',
#         'print': 'Функция input() используется в Python для считывания данных. Она всегда пишется с круглыми скобками. Когда программа доходит до места, где есть input(), она ждёт, пока пользователь введёт текст с клавиатуры (ввод завершается нажатием клавиши Enter). Введённая строка подставляется на место input().',
#         'input': 'Функция int() используется в Python для преобразования строки к целому числу. Буквально int() означает следующее: «Возьми то, что указано в качестве аргумента в скобках, и преврати это в целое число».',
#         # 'int': '',
#     }
#     subject_example = {
#         'print': 'Пример:\nprint("Привет, мир!")\nПрограмма напечатает «Привет, мир!»',
#         'input': 'Пример:\nprint("Как тебя зовут?")\nname = input()\nprint("Привет,", name)\nЕсли ввели «Роб», программа напечатает «Привет, Роб».',
#         'int': 'Пример:\nprint("Введи целое число.")\nnum = int(input())\nЕсли ввели «5», в num запишется целое число 5. Потом с ним можно будет проводить арифметические операции.',
#     }
#
#     if example:
#         print(subject_example.get(subject, ''))
#     print(f"\n{subject_text.get(subject, 'У меня пока нет описания этой команды.')}")
#     # try:
#     #     print(text[subject])
#     # except KeyError:
#     #     print('У меня пока нет описания этой команды.')
#
#
# Rob_helps()
# print()
# Rob_helps(subject='print', example=True)
# print()
# Rob_helps(subject='input', example=True)
# print()
# Rob_helps(subject='int', example=True)
# print()
# Rob_helps(subject='другое', example=True)

# def hello(name, meal):
#     print(f'{name}, приветствую тебя! Бери {meal} :)')
#
#
# hello(name=input(), meal=input())

# def count_cookies(cookies):
#     if cookies == 1:
#         print('У тебя 1 печенька')
#     elif 2 <= cookies < 4:
#         print(f'у тебя {cookies} печеньки')
#     elif 5 <= cookies <20:
#         print(f'у тебя {cookies} печенек')
#     elif 20 <= cookies <= 30:
#         print(f'Ого, сколько у тебя печенек! Целых {cookies}')
#     else:
#         print('У тебя нет печенек')
# count_cookies(cookies=int(input()))

# def count_cookies(cookies):
#     if cookies == 1:
#         return ('У тебя 1 печенька')
#     elif 2 <= cookies <= 4:
#         return (f'У тебя {cookies} печеньки')
#     elif 5 <= cookies <= 20:
#         return (f'У тебя {cookies} печенек')
#     elif 20 <= cookies:
#         return (f'Ого, сколько у тебя печенек! Целых {cookies}')
#     else:
#         return ('У тебя нет печенек')
#
#
# for i in range(30 + 1):
#     print(count_cookies(cookies=i))

# def lets_go(name= 'Друг', target = 'учить Python'):
#     print(name + ', пойдём ' + target)
#
#
# lets_go(name='Друг', target='учить Python')

# def lets_go(name='Друг', target='учить Python'):
#     print(name + ', пойдём ' + target)
#
# lets_go(target='решать задачи')


# def convert_phone_num(phone_num):
#     return ''.join([x for x in list(phone_num) if x.isdigit() or x == '+'])
#
#
# print(convert_phone_num(input()))
# assert convert_phone_num('+7(999)888-77-66')=='+79998887766'
# assert convert_phone_num('+7 987 654 32 10')=='+79876543210'

# def generate_new_mail(mail):
#     return f"{mail.split('@')[0]}@progress.ru"
#     # m = mail.split('@')
#     # m[1] = 'progress.ru'
#     # return '@'.join(m)
#
#
# print(generate_new_mail(input()))
# assert generate_new_mail('ivan_ivanov@yandex.ru') == 'ivan_ivanov@progress.ru'
# assert generate_new_mail('tatiana_smirnova@gmail.com') == 'tatiana_smirnova@progress.ru'
