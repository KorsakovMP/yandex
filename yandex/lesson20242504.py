# def square_and_cube(n):
#     return n ** 2, n ** 3
#
# print(*square_and_cube(int(input())), sep='\n')

# def add_and_multiply(a, b):
#     return a + b, a * b
#
#
# print(
#     *add_and_multiply(
#         a=int(input()),
#         b=int(input()),
#     ),
#     sep='\n'
# )

# def num_description(n):
#     if n % 2 == 0:
#         return True
#     return False
#     if n > 0:
#         return True
#     return False
# def is_positive(n):
#     if n > 0:
#         return True
#     return False
#
# n = int(input())
#
# print(
#     'положительное' if is_positive(n) else 'отрицательное',
#     'четное' if num_description(n) else 'нечетное',
#     sep='\n'
# )

# def mid_of_section(x1, x2, y1, y2):
#     return (x1 + x2 / 2) ,(y1 + y2 / 2)
#
# print(*mid_of_section(x1=int(input()), x2=int(input()), y1=int(input()), y2=int(input()),
# )

# def is_parity(n):
#     if n % 2 == 0:
#         return True
#     return False
#
# def is_positive(n):
#     if n > 0:
#         return True
#     return False
#
# def num_description(n):
#     return f"{'положительное' if is_positive(n) else 'отрицательное'}\n{'чётное' if is_parity(n) else 'нечётное'}"
#
# n = int(input())
#
# print(num_description(n))


# def min_avg_max(a=-1, b=2, c=-3):
#     return sorted([a, b, c])
#
#
# print(*min_avg_max(
#     a=int(input()),
#     b=int(input()),
#     c=int(input()),
# ), sep='\n')

# def mid_of_section(x1=1, y1=1, x2=2, y2=2):
#     return (x1 + x2) / 2 ,(y1 + y2) / 2
#
# print(*mid_of_section(
#     x1=int(input()),
#     y1=int(input()),
#     x2=int(input()),
#     y2=int(input()),
# ), sep='\n')

# import math
#
# def circle_info(r):
#     return 2 * math.pi * r, math.pi*r*r
#
# print(*circle_info(r=int(input())), sep='\n')

# def discriminant(a=1, b=-2, c=-3):
#     return b ** 2 - 4 * a * c
# print(discriminant(
#     a=int(input()),
#     b=int(input()),
#     c=int(input()),
# ))

# def equation_roots(a=1, b=-2, c=-3):
#     d = (b ** 2 - 4 * a * c) ** .5
#     return sorted([(-b + d) / (2 * a), (-b - d) / (2 * a)])
#
#
# print(
#     *equation_roots(
#     a=int(input()),
#     b=int(input()),
#     c=int(input()),
#     ), sep='\n'
# )

# def draw_triangle(n=8):
#     for i in range(n, 0, -1):
#         print('*' * i)
#
#
# draw_triangle(n=8)

# def draw_triangle():
#     n=8
#     for i in range(n, 0, -1):
#         print(' ' * (i), '*' * (n - i+1), sep='')
#
#
# draw_triangle()


# def draw_rhombus():
#     n = 8
#     for i in range(n, 0, -1):
#         print(' ' * (i-1), '*' * (2 * n - 2 * i + 1), sep='')
#     for i in range(2, n + 1):
#         print(' ' * (i-1), '*' * (2 * n - 2 * i + 1), sep='')
#
# for _ in range(3):
#     draw_rhombus()


# def lucky_ticket(n):
#     # n3 = n % 10
#     # n2 = n % 100 // 10
#     # n1 = n % 1000 // 100
#     # n0 = n % 10000 // 1000
#     #
#     # if n0 + n1 == n2 + n3:
#     #     return 'Счастье привалило!'
#     # return 'Может, в другой раз'
#
#     # n = str(n)
#
#     if int(n[0]) + int(n[1]) == int(n[2]) + int(n[3]):
#         return 'Счастье привалило!'
#     return 'Может, в другой раз'
#
#
# print(lucky_ticket(n=input()))

# def my_input():
#     i = 0
#     while not (1 <= i <= 8):
#         i = int(input())
#     return i
#
#
# def cell_color(x, y):
#     if (x + y) % 2 == 0:
#         return 'белый'
#     return 'чёрный'
#
#
# print(
#     cell_color(
#         x=int(my_input()),
#         y=int(my_input()),
#     )
# )

# def my_input():
#     i = 0
#     while not (1 <= i <= 10):
#         i = int(input())
#     return i
#
# def num_to_word(n):
#     # d = {1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять'}
#     # return d[n]
#     one_to_ten = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#     return one_to_ten[n-1]
#
# print(num_to_word(n=my_input()))

# def num_to_word(n: int, leng: str):
#     one_to_ten_ru = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#
#     one_to_ten_en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
#     return one_to_ten_ru[n - 1] if leng == 'ru' else one_to_ten_en[n - 1]
#
#
# print(num_to_word(n=int(input()), leng=input()))
