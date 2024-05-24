# num = int(input())
# total = 1
# while num != 0:
#     last_digit = num % 10
#     total *= last_digit
#     num = num // 10
# print(total)

# num = int(input())
# # total = 1
# while num != 0:
#     last_digit = num % 10
#     # total *= last_digit
#     print(last_digit)
#     num = num // 10

# num = int(input())
# # total = 1
# while num != 0:
#     last_digit = num % 10
#     # total *= last_digit
#     print(last_digit, end='')
#     num = num // 10

# num = int(input())
# last_digit = num % 10
# num = num // 10
# min_digit = last_digit
# max_digit = last_digit
# while num != 0:
#     last_digit = num % 10
#     num = num // 10
#     min_digit = min(last_digit, min_digit)
#     max_digit = max(last_digit, max_digit)
# print(f'Минимальная цифра равна {min_digit}')
# print(f'Максимальная цифра равна {max_digit}')

# num = int(input())
# count = 0
# total_sum = 0
# total_mult = 1
# while num != 0:
#     last_digit = num % 10
#     count += 1
#     total_sum += last_digit
#     total_mult *= last_digit
#     num = num // 10
# print('Количество цифр равно', count)
# print('Сумма цифр равна', total_sum)
# print('Произведение цифр равно', total_mult)

# num = int(input())
# last_digit = num % 10
#
# while num >= 10:
#     num = num // 10
#
# print(num)
# print(last_digit)

# num = int(input())
#
# while num >= 100:
#     num = num // 10
#
# print(num % 10)

num = int(input())
last_digit = num % 10

flag = True

while num >= 10:
    num = num // 10
    if num % 10 != last_digit:
        flag = False

if flag:
    print('Все цифры числа одинаковые.')
else:
    print('Не все цифры числа одинаковые.')
