# import random
#
# def random_10_numbers_1_100():
#     numbers = []
#     for i in range(10):
#         num = random.randint(1, 100)
#         numbers.append(num)
#     return numbers
# print(random_10_numbers_1_100())
import random


# import random
# def random_event():
#     return random.random(0.0)
# print(random_event())

# import random
# def flip_coin_three_times(symbol):
#     tree_symbols = []
#     for i in range(3):

# import random
# def random_even_two_digit():
#     return random.randrange(0,100, 2)
# print(random_even_two_digit())

# import random

# def two_dices():
#     result = []
#     dices = random.randint(1, 6)
#     dices2 = random.randint(1, 6)
#     result.append(dices)
#     result.append(dices2)
#     if dices > dices2:
#         result.append(1)
#     elif dices2 > dices:
#         result.append(2)
#     else:
#         result.append(0)
#     return result
#
#
# print(two_dices())

# import random
# def flip_coin_three_times():
#     result = []
#     for i in range(3):
#         coin = random.randint(0,1)
#         if coin == 0:
#             result.append('О')
#         else:
#             result.append('Р')
#     ''.join(result)
#     return result

# import random
# def random_event():
#     event = random.random()
#     return event


# import random
# def random_fractional():
#     num = random.uniform(0.99, 0.99999)
#     return num

# import random
#
#
# def shuffle_students(students: str):
#     l = students.split(' ')
#     random.shuffle(l)
#     return l
#
# print(shuffle_students('1111 2222 3333 4444 555 6666'))

# import random
#
#
# def launch_round(students: int):
#     variants = ['камень', 'ножницы', 'бумага']
#     answer = []
#     for i in range(students):
#         answer.append(random.choice(variants))
#     return answer
#
#
# print(*launch_round(int(input())), sep ='\n')

# import random
#
#
# def class_generator(numbers: list[int], letters: list[str]):
#     return f'{random.choice(numbers)}{random.choice(letters)}'
#
#
# print(class_generator([1, 2, 3, 4], ['А', 'Б']))

# import random
#
#
# # def random_marks(students: int):
# #     return [random.choice([2, 3, 4, 5]) for _ in range(students)]
#
# def random_marks(students: int):
#     answer = []
#     for _ in range(students):
#         answer.append(f'{random.choice([2, 3, 4, 5])}{random.choice(["+","-", ""])}')
#
#     return answer
#
# print(random_marks(3))

# def check_homework(homework_status: list[bool]):
#
#     # s3 = random.sample(homework_status, k=3)
#     # if s3[0] is True and s3[1] is True and s3[2] is True:
#     # if all(random.sample(homework_status, k=3)):
#     #
#     #     return 'Молодцы!'
#     # return 'Делайте дз!'
#
#     return 'Молодцы!' if all(random.sample(homework_status, k=3)) else 'Делайте дз!'
#
#
# print(
#     check_homework(
#         [
#             True,  # Ученик 1
#             True,  # Ученик 2
#             True,  # Ученик 3
#             True,  # Ученик 4
#             True,  # Ученик 5
#             True,  # Ученик 6
#             True,  # Ученик 7
#             True,  # Ученик 8
#             False,  # Ученик 9
#             False,  # Ученик 10
#             False,  # Ученик 11
#             False,  # Ученик 12
#             False,  # Ученик 13
#             False,  # Ученик 14
#             False,  # Ученик 15
#         ]
#     )
# )

import random

def check_marks(marks: list[int]):
    marks_10 = random.sample(marks, 10)
    marks_10.sort()
    if marks_10[2]>=4:
        return 'Хорошие оценки!'
    return 'Исправляй тройки!'

print(
    check_marks(
        [
            3,  # Ученик 1
            4,  # Ученик 2
            5,  # Ученик 3
            3,  # Ученик 4
            4,  # Ученик 5
            5,  # Ученик 6
            3,  # Ученик 7
            4,  # Ученик 8
            5,  # Ученик 9
            3,  # Ученик 10
            4,  # Ученик 11
            5,  # Ученик 12
            3,  # Ученик 13
            4,  # Ученик 14
            5,  # Ученик 15
        ]
    )
)