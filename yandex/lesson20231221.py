# # задай сумматор total
# total = 0
# for i in range(1, 101):
#     total += i
# # сложи числа в цикле
# print('Сумма равна', total)

# total = 1
# # задай мультипликатор total
# for i in range(1, 11):
#     total *= i
# # умножь числа в цикле
# print('Произведение равно', total)

# total = 0
# for i in range(1, 101):
#     if i ** 2 % 10 == 4:
#         total += 1
# print(total)
#
# total = 0
# m = int(input())
# n = int(input())
# for i in range(m, n):
#     if i ** 3 % 10 in (7, 8):
#         total += 1
# print(total)

# total = 0
# for i in range(int(input())):
#     total += int(input())
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 in (5, 6):
#         total += i
# print(total)

# total = 1
# n = int(input())
# for i in range(1, n + 1):
#     total *= i
# print(total)

# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

# total = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

# flag = 'Да'
# for _ in range(5):
#     n = int(input())
#     if n % 2 == 1:
#         flag = 'Нет'
# print(flag)

# num = int(input())
# total = 1
# while num != 0:
#     last_digit = num % 10
#     total *= last_digit

# total = 0
# i = 3
# while total != 'stop':
#     while i <= 9 :
#         print('Python на повторе!')
#     i += 1
# i = 0
# total = 0
# while total != 'stop':
#     while i < 10:
#         total += i

# total = 0
# for _ in range(6):
#     n = int(input())
# while n == 4:
#     if n == 4:
#         total += 1
# print(total)

text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()
print('Сумма чисел равна', total)

