# words = []
# for _ in range(3):
#     words.append(input())
#
# sort_words = sorted(words, key=len, reverse=True)
# print(f'Самое длинное слово: {sort_words[0]}')
# print(f'Слово средней длины: {sort_words[1]}')
# print(f'Самое короткое слово: {sort_words[2]}')

# words = []
# for _ in range(3):
#     words.append(input())
#
# words = [
#     '333', '22', '1',
# ]
# # for _ in range(len(words) - 1):
# run_again = True
# while run_again:
#     run_again = False
#     for i in range(len(words) - 1):
#         if len(words[i]) > len(words[i + 1]):
#             words[i], words[i + 1] = words[i + 1], words[i]
#             run_again = True
#
# print(f'Самое длинное слово: {words[0]}')
# print(f'Слово средней длины: {words[1]}')
# print(f'Самое короткое слово: {words[2]}')

# words = ['333', '22', '1']
#
# for _ in range(len(words) - 1):
#     for i in range(len(words) - 1):
#         if len(words[i]) < len(words[i + 1]):
#             words[i], words[i + 1] = words[i + 1], words[i]
#
# print(f'Самое длинное слово: {words[0]}')
# print(f'Слово средней длины: {words[1]}')
# print(f'Самое короткое слово: {words[2]}')

# while True:
#     words = []
#     for _ in range(3):
#         words.append(len(input()))
#
#     if words[0] == words[1] == words[2]:
#         print('Все три слова одной длины.')
#     else:
#         break

# letters = []
# sentensice = input().lower()
# for char in sentensice:
#     if char in 'аеёиоуыэюя':
#         letters.append(char)
# print(', '.join(letters))

# string = input()
# print(string[:5])
# print(string[5:])
# print(string[-5:])
# print(string[:-5])
# print(string[::5])

# n = int(input())
# print([-n+i for i in range(n+1)])

# numbers = [1, 2, 3, 4]
# print(f'Сумма чисел списка: {sum(numbers)}')
# print(f'Среднее арифметическое: {sum(numbers) / len((numbers))}')

# n = int(input())
# numbers = []
# for i in range(3):
#     numbers.append(float(input()))
# print(numbers)
# print([float(input()) for _ in range(int(input()))])

# string = input()
# print(string)
# print()
# for number in string.split():
#     print(number)

# numbers = input()
# numbers1 = []
# for number in numbers.split():
#     if int(number) > 0:
#         numbers1.append(int(number))
# print(numbers1)

# result = []
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(len(alphabet)):
#     index = len(alphabet) - i -1
#     result.append(alphabet[index]*(index+1))
# print(result)


# print(' '.join([str(int(i) ** 2) for i in input().split() if int(i) % 2 == 1]))

# letter = input()
# string = input()
# for name in string.split():
#     if letter.lower() in name.lower():
#         print(name)

# month = {
#     1: 'января',
#     2: 'февраля',
#     3: 'марта',
#     4: 'апреля',
#     5: 'мая',
#     6: 'июня',
#     7: 'июля',
#     8: 'авруста',
#     9: 'сентября',
#     10: 'октября',
#     11: 'ноября',
#     12: 'декабря',
# }
# d, m, y = input().split('.')
# print(f'{int(d)} {month[int(m)]} {y}')