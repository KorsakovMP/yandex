# number = int(input())
# numbers = []
# for i in range(-number, number+ 1):
#     numbers.append(i)
# print(numbers)

# proposal = input()
# print([x for x in range(len(proposal))])

# average = sum(numbers)/ len(numbers)
# print(f'Среднее арифметическое: {average}')
# bigger_average = []
# smaller_average = []
# for number in numbers:
#     if number > average:
#         bigger_average.append(number)
#     elif number < average:
#         smaller_average.append(number)
# print(f'Числа больше среднего: {bigger_average}')
# print(f'Числа меньше среднего: {smaller_average}')

# letter_list = list(letters)
# print(''.join(letter_list[::-1]))

# numbers = [2, -1, 0, -3, 4]
# print(['+' if x > 0 else '-' if x < 0 else 0 for x in numbers])

# list1 = ['поспать']
# list2 = ['погулять', 'почитать']
# print(list1 * 5 + list2 * 3)

# n = int(input())
# print([x for x in range(n, 2 * n + 1)])
# print([2 * n for _ in range(n)])
# print([x for x in range(-2 * n, -n + 1)])

# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
# for month in months:
#     print(month)
# print('\n'.join(months))

# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
# print(*months)
# print('Январь', 'Февраль', 'Март', 'Апрель', 'Май')

# months = ['Январь', '01', 'Февраль', '02', 'Март', '03']
# for i in range(len(months)):
#     if i % 2 == 0:
#         print(months[i])

# numbers = [1, 2, 3, 4, 5]
# print('(', end='')
# print(*numbers, sep=' + ', end='')
# print(') ** 2 =', sum(numbers) ** 2)

# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers) - 1):
#     print(f"({numbers[i]} + {numbers[i + 1]}) ** 2 = {(numbers[i]+numbers[i+1]) ** 2}")

# names = ['Полина', 'Роман', 'Кристина', 'Денис', 'Варвара']
# for name in names:
#     if 'и' not in name.lower():
#         print(name)

# names = ['Вячеслав', 'Станислав', 'Ярослав']
# max_name = ''
# for name in names:
#     if len(name) > len(max_name):
#         max_name = name
# print(f'Самое длинное имя: {max_name}')