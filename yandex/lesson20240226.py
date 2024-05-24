# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
# print(len(odd_numbers))
# print(odd_numbers[0:8])
# print(odd_numbers[1: 7])

# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
# print(len(odd_numbers))
# print(odd_numbers[::-1])
# print(odd_numbers[1:-1])

# result = []
# n = int(input())
# for i in range(n):
#     s = input()
#     result.append(s)
# print(result)

# result = []
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for i in range(len(alphabet)):
#     result.append(alphabet[i] * (i+1))
# print(result)

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# print(alphabet[1]*2)

# result = []
# n = int(input())
# for i in range(n):
#     n = float(input())
#     result.append(int(n))
# print(result)


# result = []
# n = int(input())
# for i in range(n):
#     n = input()
#     result.append(int(n)**2)
# print(result)

# result = []
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         result.append(i)
# print(result)

# result = []
# result2 = []
# n = int(input())
# for i in range(n):
#     result.append(int(input()))
#
# for i in range(n - 1):
#     result2.append(result[i] * result[i + 1])
#
# print(result2)

# result = []
# n = int(input())
# for i in range(n):
#     result.append(int(input()))
#
# for i in range(n - 1, -1, -1):
#     if i % 2 == 0:
#         del result[i]
# print(result)

# result = []
# n = int(input())
# for i in range(n):
#     string = input()
#     for s in string:
#         result.append(s)
# print(result)

# vowels = ['а', 'и', 'о', 'у', 'ы', 'э']
# vowels.insert(1, 'е')
# vowels.insert(2, 'ё')
# vowels.insert(8, 'ю')
# vowels.insert(9, 'я')
# print(vowels)

# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# print(alphabet.index('ф'))

# odd_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in odd_numbers:
#     if number % 2 == 0:
#         odd_numbers.remove(number)
# print(odd_numbers)

# food = ['хлеб', 'сыр', 'творог', 'сок', 'морс']
# print(food[:3])
# print(food.pop(3))
# print(food.pop(3))

# zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(zeros.count(0))

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.reverse()
# print(numbers)

# zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# zeros.clear()
# print(zeros)

# flags = [True, False]
# flags_copy = flags.copy()
# print(flags)
# print(flags_copy)
# flags.append(1)
# print(flags_copy)

# names = ['Евгений', 'Регина', 'Игорь', 'Татьяна', 'Леонид', 'Марина', 'Андрей', 'Полина', 'Денис', 'Кристина', 'Роман', 'Варвара']
# names.sort(reverse=True)
# print(names)

# for s in range(5):
#     print(s)