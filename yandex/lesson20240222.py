# numbers = [-132, 213, -321, -312, 231, -123]
# for i in range(len(numbers)):
#     if numbers[i] >= 0:
#         print(numbers[i], end='\n')

# trees = ['сосна', 'дуб', 'липа', 'клён', 'берёза', 'тополь']
# print(*trees, sep='\n')

# trees = ['сосна', 'дуб', 'липа', 'клён', 'берёза', 'тополь']
# for num in trees:
#     print(num, end=' ')


# s = input()
# print(*s, end='\n\n')
# print(*s, sep='\n')

# sum = 0
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     sum += num ** 3
# print(sum)

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(3 * num ** 2 -4 * num + 5)

# numbers = [-132, 213, -321, -312, 231, -123]
# _max = max(numbers)
# _min = min(numbers)
# for n in numbers:
#     if n not in (_min, _max):
#         print(n)

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for num in alphabet:
#     print(num, end=' ')

# vowels = 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'
# consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# print(f'Гласные:', *vowels)
# print(f'согласные:', *consonants)


# names = ['Евгений', 'Регина', 'Игорь', 'Татьяна', 'Леонид', 'Марина', 'Андрей', 'Полина', 'Денис', 'Кристина', 'Роман', 'Варвара']
# for name in names:
#     # print(name, name.upper())
#     if 'Р' in name or 'р' in name:
#         print(name)
#
# cat1 = ['Мурка', 2.7, 'рыжая']
# cat2 = ['Снежок', 1.5, 'белый']
# cat3 = ['Ласка', 3.6, 'серая']
# cats = [*cat1, *cat2, *cat3]
# cats2 = cat1+cat2+cat3
# print(*cats, sep='\n')
# print(cats2)

# n = input()
# print(n.split())

# _str = input()
# for s in _str.split():
#     print(s[0], end='.')
# #
# # ss = _str.split()
# # print(f'{ss[0][0]}.{ss[1][0]}.{ss[2][0]}.')

# nums = input()
# for num in nums.split():
#     print(int(num) * '*')

# nums = input()
# print(nums.split())

# nums = input()
# if len(nums.split('.')) == 4:
#     valid = True
#     for num in nums.split('.'):
#         if 0 > int(num) or int(num) > 255:
#             valid = False
#             break
# else:
#     valid = False
#
# if valid:
#     print('Да')
# else:
#     print('Нет')

# nums = input()
# separator = input()
# print(separator.join(nums))
