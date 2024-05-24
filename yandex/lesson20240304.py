# n = int(input())
# a = list()
# for i in range(n):
#     word = input()
#     if word in a:
#         continue
#     else:
#         print(word)
#         a.append(word)


# n = int(input())
# sentences = list()
# for _ in range(n):
#     sentences.append(input())
# word = input()
#
# for sentence in sentences:
#     if word.upper() in sentence.upper():
#         print(sentence)

# n = int(input())
# positive = []
# zero = []
# negative = []
# for _ in range(n):
#     number = int(input())
#     if number == 0:
#         zero.append(str(number))
#     elif number > 0:
#         positive.append(str(number))
#     else:
#         negative.append(str(number))
# print(' '.join(negative))
# print(' '.join(zero))
# print(' '.join(positive))
#
# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# print(' '.join([str(number) for number in numbers if int(number) < 0]))
# print(' '.join([str(number) for number in numbers if int(number) == 0]))
# print(' '.join([str(number) for number in numbers if int(number) > 0]))

# str_numbers = input()
# numbers = [int(number) for number in str_numbers.split()]
#
# max_value = max(numbers)
# max_index = numbers.index(max_value)
#
# min_value = min(numbers)
# min_index = numbers.index(min_value)
#
# numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
#
# print(' '.join([str(number) for number in numbers]))

# print(input().upper().count(input().upper()))

# s1 = 'a = int(input())  # пользователь вводит целое число a'
# print(s1.split('#')[0].rstrip())

# for _ in range(int(input())):
#     print(input().split('#')[0].rstrip())

# str_numbers = input()
# numbers = [int(number) for number in str_numbers.split()]
# print(' '.join([str(number) for number in sorted(numbers)]))
# print(' '.join([str(number) for number in sorted(numbers, reverse=True)]))

# n = int(input())
# numbers_first = []
# numbers_second = []
# for i in range(n):
#     number = int(input())
#     if number not in numbers_first:
#         numbers_first.append(number)
#     else:
#         if number not in numbers_second:
#             print(number)
#             numbers_second.append(number)
#
# n = int(input())
# numbers_count = {}
# for _ in range(n):
#     number = int(input())
#     numbers_count[number] = numbers_count.get(number, 0) + 1
#     if numbers_count[number] == 2:
#         print(number)


# # Счмтываем все предложения
# sentences = list()
# for _ in range(int(input())):
#     sentences.append(input())
# # sentences = [
# #     'семейные фильмы',
# #     'СМОТРЕТЬ ФИЛЬМЫ ОНЛАЙН',
# #     'фантастические сериалы'
# # ]
#
# # Счтываем все поисковые слова
# words = list()
# for _ in range(int(input())):
#     words.append(input())
# # words = [
# #     'Фильмы',
# #     'Онлайн'
# # ]
#
#
# for sentence in sentences:
#     find = True
#     for word in words:
#         if word.upper() not in sentence.upper():
#             find = False
#             break
#     if find:
#         print(sentence)

# soglas = []
# glas = []
# for _ in range(int(input())):
#     word = input()
#     if word[0].lower() in 'аеёиоуыэюя':
#         glas.append(word)
#     elif word[0].lower() in 'бвгджзйклмнпрстфхцчшщ':
#         soglas.append(word)
# print(' '.join(glas))
# print(' '.join(soglas))

# words = []
# for i in range(int(input())):
#     if i == 0:
#         sentence = input()
#     words.append(input())
#
# find = True
# for word in words:
#     if word not in sentence:
#         find = False
#         break
#
# if find:
#     print('Да')
# else:
#     print('Нет')

# for i in range(int(input())):
#     line = input()
#     if '#' in line:
#         print(f"#{line.split('#')[1]}")

# print('print("Привет,", name)  # программа выводит строку "Привет," с именем пользователя'.split('#')[-1])

str_words = input()
print(' '.join(sorted(str_words.split())))
print(' '.join(sorted(str_words.split(), reverse=True)))
