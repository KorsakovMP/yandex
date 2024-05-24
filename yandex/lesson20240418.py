# функция перевода градусов
# def convert_to_celsius(temp):
#     return 5 / 9 * (temp - 32)
#
#
# # основная программа
# temp = float(input())  # градусы Фаренгейта
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия

# def convert_grade(grade):
#     result = -1
#     if grade >= 90:
#         result = 5
#     elif grade >= 80:
#         result = 4
#     elif grade >= 70:
#         result = 3
#     elif grade >= 60:
#         result = 2
#     else:
#         result = 1
#     return result
#
#
# print(f'Введите отметку по 100-балльной системе: {convert_grade(grade=int(input()))}')

###########################################################################
# def get_days(month):
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return days[month-1]
#
# # print(get_days(month=1))
# # print(get_days(month=2))
# # print(get_days(month=3))
# # print(get_days(month=4))
# # print(get_days(month=5))
# print(get_days(month=int(input())))

# def get_average(x, y, z):
#     return (x + y + z) / 3
# avereng = get_average(x=int(input()),y=int(input()),z=int(input()))
# print(f'Среднее значение равно {avereng}')
# print(avereng)

# def len_of_section(a,b):
#     return b - a
# print(len_of_section(a=int(input()), b=int(input())))

# def calculate_time():
#     distance = float(input())
#     speed = float(input())
#     time = distance / speed
#     return time
# print(calculate_time())

# def convert_to_miles(kilometers):
#     return kilometers * 0.6214
# print(convert_to_miles(kilometers=float(input())))

# def get_dividers(divider):
#     return [i for i in range(1, divider+1) if divider % i == 0]
# print(get_dividers(int(input())))

# def num_of_dividers(divider):
#     return len([i for i in range(1, divider+1) if divider % i == 0])
# print(num_of_dividers(int(input())))

# def find_all(string, symbol):
#     anser = []
#     for i in range(len(string)):
#         if string[i] == symbol:
#             anser.append(i)
#     return anser
#
#
# print(
#     find_all(
#         string=input(),
#         symbol=input()
#     )
# )

