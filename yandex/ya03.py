# number = int(input())
# hundreds = (number % 1000) // 100
# thousands = number // 1000
#
# if thousands == 0 and hundreds > 0:
#     print('Да')
# else:
#     print('Нет')


# if len(input()) == 4:
#     print('Да')
# else:
#     print('Нет')

# number = int(input())
# ones = number % 10
# tens = (number % 100) // 10
# hundreds = (number % 1000) // 100
#
# if ones == tens or ones == hundreds or tens == hundreds:
#     print('Нет')
# else:
#     print('Да')

# numbers = set()
# s = input()
# for n in s:
#     numbers.add(n)
# if len(numbers) == len(s):
#     print('Да')
# else:
#     print('Нет')
#

# number = int(input())
# if 3  <= number <= 7 or 15 <= number <= 21:
#     print('Да')
# else:
#     print('Нет')

# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# elif x > 0 and y < 0:
#     print('4 четверть')

# num = int(input())
# num = 8989
# num = 4567
# a = num // 1000
# b = (num % 1000) // 100
# c = (num % 100) // 10
# d = num % 10
# if a == b or a == c or a == d or b == c or b == d or c == d:
#     print('Да')
# else:
#     print('Нет')

# x = int(input())
# y = int(input())
# if (x > 0 and y > 0) or (x < 0 and y < 0):
#     print('Да')
# else:
#     print('Нет')

# num1 = 17
# num2 = 18
# if num1 // 3 < 5 or num1 > num2 and num2 % 3 == 0:
#     print('Да')
# else:
#     print('Нет')

# number = int(input())
# if 5 <= number <= 9 or 26 <= number <= 30:
#     print('Да')
# else:
#     print('Нет')

# h = int(input())
# m = int(input())
#
# if h == 15 and m in (0, 30):
#     print('Да')
# else:
#     print('Нет')

# age = int(input())
# answer = input()
#
# if age >= 18 and answer == 'Да':
#     print('Подходит')
# else:
#     print('Не подходит')

# x1 = input()
# y1 = input()
# x2 = input()
# y2 = input()
#
# if x1 == x2 or y1 == y2:
#     print('Да')
# else:
#     print('Нет')

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if x2 in (x1 - 1, x1, x1 + 1) and y2 in (y1 - 1, y1, y1 + 1):
# # if x1 - 1 <= x2 <= x1 + 1 and y1 - 1 <= y2 <= y1 + 1:
#     print('Да')
# else:
#     print('Нет')

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if any(
#         [
#             x1 == x2 + 1 and y1 == y2 + 2,
#             x1 == x2 + 2 and y1 == y2 + 1,
#
#             x1 == x2 - 1 and y1 == y2 + 2,
#             x1 == x2 - 2 and y1 == y2 + 1,
#
#             x1 == x2 + 1 and y1 == y2 - 2,
#             x1 == x2 + 2 and y1 == y2 - 1,
#
#             x1 == x2 - 1 and y1 == y2 - 2,
#             x1 == x2 - 2 and y1 == y2 - 1,
#         ]
# ):
#     print('Да')
# else:
#     print('Нет')

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if x1 + y1 == x2 + y2 or x1 - x2 == y1 - y2 or x1 == x2 or y1 == y2:
#     print('Да')
# else:
#     print('Нет')

# hours = int(input())
# minutes = int(input())
# if hours in (10, 11) and minutes == 30:
#     print('Да')
# else:
#     print('Нет')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# print((x1 + y1) % 2)
# print((x2 + y2) % 2)
# if x1 + y1 + x2 + y2 % 2 = 0
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print('Да')
else:
    print('Нет')
