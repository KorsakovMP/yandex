# def box_volume(a, b, c):
#     V = a * b * c
#     return  V

# def divide(a, b):
#     return divmod(a, b)
#     # return a // b, a % b

# def decode(word: str):
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     return ''.join([alphabet[int(i)-1] for i in word.split()])
#
# assert decode('1 2 3') == 'абв'

# def num_of_letter(letter: str):
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     return alphabet.find(letter)+1
#
# assert num_of_letter('а') == 1

# def draw_triangle():
#     anser = ''
#     for i in range(3):
#         anser += ' ' * (2 - i)
#         anser += '*' * (1 + i * 2)
#         anser += '\n'
#     return anser
#
#
# print(draw_triangle())
