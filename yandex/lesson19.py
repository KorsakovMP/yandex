# n = int(input())
# sum = 0
# for i in range(n):
#     sum += i + 1
# print(sum)


# amount = 0
# for _ in range(10):
#     i = input()
#     if i == 'Да':
#         amount += 1
# print(amount)

# for n in range(5):
#     name = input()
#     age = input()
#     print(f'{n+1}. {name}, возраст: {age}')

# for n in range(9):
#     print((n + 1) * str(n + 1))

# a = input()
# m = int(input())
# n = int(input())
# for _ in range(n):
#     print(m * a)

# m = int(input())
# n = int(input())
# if m < n:
#     r = range(m, n + 1)
# else:
#     r = range(m, n - 1, -1)
#
# for i in r:
#     print(i)

for i in range(75, 100):
    if i % 2 == 0 and i % 3 == 0 or i % 10 == 2 or i % 10 == 3:
        print(i)

# n = int(input())
# for m in range(10):
#     print(f'{n} x {m + 1} = {(m + 1) * n}')
