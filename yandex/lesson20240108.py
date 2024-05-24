# num = int(input())
# num_for_while = num
# flag = True
#
# while num_for_while > 0:
#     if num_for_while % 10 == 0:
#         flag = False
#         break
#     num_for_while = num_for_while // 10
#
# if flag:
#     print(f'Число {num} не содержит цифру 0')
# else:
#     print(f'Число {num} содержит цифру 0')

# while True:
#     print('Я зациклился!')
#     break

# num = int(input())
# for i in range(2, num):
#     if num % i == 0:
#         print(i)
#         break

# n = int(input())
# for i in range(1, n + 1):
#     if 10 < i < 30:
#         continue
#     elif 50 < i < 60:
#         continue
#     elif 80 < i < 90:
#         continue
#     print(i)

# n = 0
# while n < 6:
#     n += 2
#     print(n)

# n = 0
# for i in range(10):
#     n += 1
#     print(i)

# i = 0
# for i in range(101):
#     if i % 7 == 0:
#         print(i)
#         i += 1

# for i in range(1, 31):
#     print(31 - i)

# counter = 0
# total = 1
# for i in range(1, 11):
#     x = int(input())
#     if x > 0:
#         total += x
#         counter += 1
# if counter > 0:
#     print(x)
#     print(total)
# else:
#     print('Неотрицательных чисел нет.')

# counter = 0
# total = 0
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         total += x
#         counter += 1
# if counter > 0:
#     print(counter)
#     print(total)
# else:
#     print('Неотрицательных чисел нет.')

# i = 1
# while i < 101:
#     if i % 7 == 0:
#         print(i)
#     i += 1

# total = 0
# for i in range(1, 51):
#     if i % 2 == 1:
#         total += i
# print(total)

# total = 1
# for i in range(7):
#     num = int(input())
#     if num % 2 == 0:
#         total *= num
# print(total)

# num = int(input())
# while num > 10:
#     num = num // 10
# print(num)

# num = int(input())
# # num = 123
# total = 1 # 3
# while num >= 1:
#     digit = num % 10
#     total *= digit
#     num //= 10
# print(total)

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(hour, ':', minute, ':', second)
