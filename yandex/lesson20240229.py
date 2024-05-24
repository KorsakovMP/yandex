# double_alphabet = ['аа', 'бб', 'вв', 'гг', 'дд', 'ее', 'ёё', 'жж', 'зз', 'ии', 'йй', 'кк', 'лл', 'мм', 'нн', 'оо', 'пп', 'рр', 'сс', 'тт', 'уу', 'фф', 'хх', 'цц', 'чч', 'шш', 'щщ', 'ъъ', 'ыы', 'ьь', 'ээ', 'юю', 'яя']
#
# alphabet = [letters[1] for letters in double_alphabet]
#
# # alphabet1 = []
# # for letters in double_alphabet:
# #     alphabet1.append(letters[1])
#
#
# print(alphabet)
# # print(alphabet1)

# # list_string = []
# string = 'Привет, мир!'
# # for letter in string:
# #     list_string.append(letter*3)
#
# list_string = [letter*3 for letter in string]

# print([letter*3 for letter in input()])


# names = ['Евгений', 'Регина', 'Игорь', 'Татьяна', 'Леонид', 'Марина', 'Андрей', 'Полина', 'Денис', 'Кристина', 'Роман', 'Варвара']
# lengths = [len(name) for name in names]
# print(lengths)

# names = ['Евгений', 'Регина', 'Игорь', 'Татьяна', 'Леонид', 'Марина', 'Андрей', 'Полина', 'Денис', 'Кристина', 'Роман', 'Варвара']
# long_names = [name for name in names if len(name) > 6]
# print(long_names)

# for i in range(100, 1001):
#     if str(i) == str(i)[::-1]:
#         print(i)

# print([i for i in range(100, 1001) if str(i) == str(i)[::-1]])

# print('\n'.join(input().split()))

# print(' '.join([str(i ** 2) for i in range(1, int(input())+1)]))

# print('\n'.join([str(int(number) ** 3) for number in input().split()]))

