# l1 = len(input())
# l2 = len(input())
# if l1 > l2:
#     print('Первое слово длиннее второго.')
# elif l1 < l2:
#     print('Второе слово длиннее первого.')
# else:
#     print('Длины слов равны.')

# string1 = input()
# string2 = input()
# if string1 == string2:
#     print('Это одинаковые слова.')
# elif string1 in string2:
#     print('Первое слово входит во второе.')
# elif string2 in string1:
#     print('Второе слово входит в первое.')
# else:
#     print('Ни одно слово не входит в другое.')

# while True:
#     s = input()
#     if len(s) != 5:
#         break
#     print(s)

# n = int(input())
# while True:
#     s = input()
#     if len(s) != n:
#         break
#     print(s)

# string = ''
# max_string = string
# while string != 'стоп':
#     string = input()
#     if len(max_string) < len(string):
#         max_string = string
# print(max_string)

# string = ''
# min_string = string
# while string != 'стоп' or string != 'Стоп':
#     string = input()
#     if len(min_string) > len(string):
#         min_string = string
# print(min_string)


# while True:
#     string1 = input()
#     string2 = input()
#     if string1 in string2:
#         print(f'{string1} входит в {string2}')
#     elif string2 in string1:
#         print(f'{string2} входит в {string1}')
#     else:
#         break

# string = ''
# min_string = string
# while string not in ('стоп', 'Стоп'):
#     if len(min_string) > len(string) or min_string == '':
#         min_string = string
#     string = input()
# print(min_string)

# master_word = input()
# while True:
#     word = input()
#     if master_word in word:
#         print(f'{master_word} входит в {word}')
#     else:
#         print(f'{master_word} не входит в {word}')
#
#         break