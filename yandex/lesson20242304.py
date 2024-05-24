# def is_even(num):
#     if num % 2 == 0:
#         return f'Число {num} чётное.'
#     else:
#         return f'Число {num} нечётное.'
#
# for _ in range(3):
#     print(is_even(int(input())))

# def is_incorrect(school=12):
#     if school not in (123, 456, 789):
#         print('Программа работает только со школами 123, 456 и 789.')
#         return False
#     return True
#
#
# def input_school():
#     while True:
#         school = int(input())
#         if is_incorrect(school=school):
#             return school
#
#
# print(f'Школа первого ученика: {input_school()}')
# print(f'Школа второго ученика: {input_school()}')
# print(f'Школа третьего ученика: {input_school()}')

# def correct_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#         return True
#     return False
# print(correct_triangle(int(input()), int(input()), int(input())))

# def is_prime(number):
#     if number % 3 == 0:
#         return False
#     return True
# print(is_prime(int(input())))

# def next_prime(number):
#     if number % 3 == 0:
#         return False
#     return True

# def right_triangle(a, b, c):
#     if a ** 2 + b ** 2 == c ** 2:
#         return True
#     return False
# print(right_triangle(int(input()), int(input()), int(input())))

# def same_symbols(words):
#     if words[len(words) / 2 ::0] == words[0::len(words) / 2]:
#         return True
#     return False
# print(same_symbols(input()))

# def without_hissing(proposal):
#     for l in proposal:
#         if l in ('ж', 'ш', 'ч', 'щ'):
#             return False
#     return True
#
#
# print(without_hissing(
#     input()
# ))

# def next_prime(n):
#     natural_number = 2
#     i = 2
#     while natural_number <= n:
#         for j in range(2, i):
#             if i % j == 0:
#                 # если делитель найден, число не простое.
#                 break
#         else:
#             natural_number = i
#         i += 1
#     return natural_number
# print(next_prime(int(input())))

# def strong_password(password):
#     if len(password) < 10:
#         return False
#
#     upper_count = 0
#     lower_count = 0
#     digit_count = 0
#
#     for l in password:
#         if l.isupper():
#             upper_count += 1
#         if l.islower():
#             lower_count += 1
#         if l.isdigit():
#             digit_count += 1
#
#     if upper_count == 0:
#         return False
#     if lower_count == 0:
#         return False
#     if digit_count == 0:
#         return False
#     return True
#
# print(strong_password(input()))

# def is_palindrome(proporsal):
#     lst = []
#     for l in proporsal:
#         if l.isalpha():
#             lst.append(l.lower())
#     if lst == lst[::-1]:
#         return True
#     return False
#
#
# print(is_palindrome(input()))

# def same_symbols(simbols):
#     for simbol in simbols:
#         if simbols[0] != simbol:
#             return False
#     return True
# print(same_symbols(input()))

# def correct_phone_num(phone_number):
#     if len(phone_number) != 12:
#         return False
#
#     country_code, number = phone_number[:2], phone_number[2:]
#
#     if country_code != '+7':
#         return False
#
#     for numb in number:
#         if not numb.isdigit():
#             return False
#
#     return True
#
#
# print(correct_phone_num(input()))

# def correct_password(password):
#     if len(password.split('_')) != 3:
#         return False
#
#     a, b, c = password.split('_')
#
#     if int(a) % 2 != 0:
#         return False
#
#     if b != b[::-1]:
#         return False
#
#     if len(c) != 3:
#         return False
#
#     return True
#
#
# print(correct_password(input()))
# print(correct_password('12_343_567'))
# print(correct_password('25_404_123'))


# def add_spaces(words):
#     lst = []
#     for s in words:
#         if s.isupper():
#             # lst.append(f' ')
#             lst.append(f' {s.lower()}')
#         else:
#             lst.append(s)
#         # lst.append(s.lower())
#
#     return ''.join(lst).strip()
#
#
# # def add_spaces2(words):
# #     lst = ''
# #     for s in words:
# #         if s.isupper():
# #             lst+=' '
# #         lst+=s.lower()
# #
# #     return lst.strip()
#
# print(add_spaces(input()))


# def correct_brackets(string):
#     count_brackets = 0
#     for s in string:
#         if s == '(':
#             count_brackets += 1
#         if s == ')':
#             count_brackets -= 1
#             if count_brackets < 0:
#                 return False
#
#     if count_brackets != 0:
#         return False
#
#     return True
#
#
# print(correct_brackets(input()))
# print(correct_brackets('print()'))
# print(correct_brackets('int(input()'))
# print(correct_brackets('((()))'))
# print(correct_brackets('()()()'))
# print(correct_brackets('()(()'))
