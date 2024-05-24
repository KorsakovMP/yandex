# Line 1 differs: out:
# >Терпение и труд<
# corr:
# >всё перетрут!<
# string = 'Терпение и труд всё перетрут!'
# print(string[:-14])


# string = 'Терпение и труд всё перетрут!'
# print(string[-13:])

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# print(alphabet[::5])

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# print(alphabet[::-1])

# string = input()
# if string == string[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# string = input()
# print(string[::2])
# print(string[1::2])

# string = input()
# print(string[:3])
# print(string[3:])
# print(string[-3:])
# print(string[:-3])
# print(string[::3])

# # string = 'информатика'
# string = 'алгебра'
# # string = input()
# l1, l2 = divmod(len(string), 2)
# print(f'{string[l1+l2:]}{string[:l1+l2]}')

# string = input()
# if string == string.title():
#     print('Регистр верный')
# else:
#     print('Регистр неверный')

# string = input()
# if 'роб' in string.lower():
#     print('«Роб» нашёлся :)')
# else:
#     print('«Роба» не нашлось :(')

# count = 0
# string = input()
# for s in string:
#     if s.isupper():
#         count += 1
# print(count)

# # count = 0
# string = 'Проходим методы строк.'
# # for s in string:
# #     if s.i
# #         count += 1
#
# print(input().count(' ') + 1)

# counta = 0
# countb = 0
# countc = 0
# string = input()
# for s in string:
#     if s in ['А', 'а']:
#         counta += 1
#     elif s in ['Б', 'б']:
#         countb += 1
#     elif s in ['В', 'в']:
#         countc += 1
# print(f'Вход А: {counta}')
# print(f'Вход Б: {countb}')
# print(f'Вход В: {countc}')
#
# string = 'бббАааБвВ'#input()
# print(f"Вход А: {string.count('А') + string.count('а')}")
# print(f"Вход Б: {string.count('Б') + string.count('б')}")
# print(f"Вход В: {string.count('В') + string.count('в')}")

import collections

string = input()#'we learn python language'
max_count = 0
max_count_literal = ''
for s in string:
    count = string.count(s)
    if s.isalpha() and max_count < count:
        max_count = count
        max_count_literal = s
print(max_count_literal)

# string = input()#'ya.ru'
# if string.endswith('.com'):
#     print('Да')
# else:
#     print('Нет')