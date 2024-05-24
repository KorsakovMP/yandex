# def draw_triangle():
#     for i in range(1 ,5 + 1):
#         print(str(i) * i)
# draw_triangle()
# print()
# draw_triangle()
# print()
# draw_triangle()

# n = int(input())
#
#
# def draw_triangle():
#     for i in range(1, n + 1):
#         print(str(i) * i)
#
#
# draw_triangle()

# def draw_triangle(base, symbol):
#     if base % 2 == 0:
#         base += 1
#
#     for i in range(1, base + 1):
#         if i < (base / 2) + 1:
#             print(symbol * i)
#         else:
#             print(symbol * (base - i + 1))
#
#
# draw_triangle(symbol=input(), base=int(input()))

# def print_fio(first_name: str, middle_name: str, last_name: str):
#     return f'{last_name[0].upper()}{first_name[0].upper()}{middle_name[0].upper()}'
#
#
# last_name = input()
# first_name = input()
# middle_name = input()
#
# print(print_fio(last_name=last_name, first_name=first_name, middle_name=middle_name))

# def len_without_spaces(words):
#     print(len(words) - words.count(' '))
#
#
# len_without_spaces(input())

# def max_digit():
#     numbers = input().split()
#     max_number = max(numbers)
#     print(max_number)
# max_digit()


# def max_digit(s='123'):
#     return max(map(int, list(s)))
#
#
# print(max_digit(input()))

# def digit_sum(s=123):
#     return sum(map(int, list(s)))
#
# print(digit_sum(input()))

# def digit_root(s=123):
#     d = sum(map(int, list(s)))
#     if d < 10:
#         return d
#     else:
#         return digit_root(str(d))
#
#
# print(digit_root(input()))

# def digit_mult(s='4554'):
#     p = 1
#     for i in map(int, list(s)):
#         p *= i
#     print(p)
# digit_mult(input())

# import math
#
#
# def circle_area(r):
#     return r ** 2 * math.pi
#
#
# print(circle_area(r=int(input())))
