user_notes = ['Первая заметка']


def calculate():
    num_1 = int(input('Введи первое число: '))
    num_2 = int(input('Введи второе число: '))
    operation = ''
    while operation not in ('+', '-', '*', '/', '//', '^'):
        operation = input(
            'Напиши, какую операцию ты хочешь выполнить (+, -, *, /, //(деление с остатком), ^(возведение в степень): '
        )
    if operation == '+':
        print(num_1 + num_2)
    if operation == '-':
        print(num_1 - num_2)
    if operation == '*':
        print(num_1 * num_2)
    if operation == '/':
        if num_2 == 0:
            print(f'{num_1}/{num_2} На ноль делить нельзя')
        else:
            print(num_1 / num_2)
    if operation == '^':
        print(num_1 ** num_2)
    if operation == '//':
        if num_2 == 0:
            print(f'{num_1}/{num_2} На ноль делить нельзя')
        else:
            print(f'Частное={num_1 // num_2} остаток={num_1 % num_2}')


def convert_for_weight():
    value = int(input('Введите значение для массы без еденицы измерения: '))

    in_unit_of_measurement = ''
    while in_unit_of_measurement not in ('г', 'кг', 'т', 'ц'):
        in_unit_of_measurement = input('Введите каких еденицах измерения значение: ')

    out_unit_of_measurement = ''
    while out_unit_of_measurement not in ('г', 'кг', 'т', 'ц'):
        out_unit_of_measurement = input('Введите в какую величину конвертируем: ')

    weight_convert_value = {
        'г': 1,
        'кг': 1000,
        'т': 1000000,
        'ц': 100000
    }

    print(value * weight_convert_value[in_unit_of_measurement] / weight_convert_value[out_unit_of_measurement])


def convert_for_distance():
    value = int(input('Введите значение для расстояния без еденицы измерения: '))

    in_unit_of_measurement = ''
    while in_unit_of_measurement not in ('м', 'км', 'см', 'мм'):
        in_unit_of_measurement = input('Введите каких еденицах измерения значение: ')

    out_unit_of_measurement = ''
    while out_unit_of_measurement not in ('м', 'км', 'см', 'мм'):
        out_unit_of_measurement = input('Введите в какую величину конвертируем: ')

    distance_convert_value = {
        'м': 1,
        'мм': 0.001,
        'см': 0.01,
        'км': 1000,
    }

    print(value * distance_convert_value[in_unit_of_measurement] / distance_convert_value[out_unit_of_measurement])


def decision():
    """
    функция решения квадратного уравнения.
    :return:
    """
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    d = b ** 2 - 4 * a * c
    print(f'{d=}')
    if d < 0:
        print('корней нет')
        return
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
    print('x1=', x1)
    print(f'{x2=}')


def manage_notes():
    global user_notes

    for index, value in enumerate(user_notes):
        print(index, value)

    while True:

        action = ''
        while action not in ('1', '2', '3'):
            action = input('Вы можете (1) добавить/ (2) удалить заметки/ (3) выход: ')

        if action == '1':
            user_notes.append(input('введите текст заметки: '))
            print('заметка успешно добавлена')

            for index, value in enumerate(user_notes):
                print(index, value)

        elif action == '2':
            index = int(input('Номер сообщения для удаления: '))
            user_notes.pop(index)

            for index, value in enumerate(user_notes):
                print(index, value)

        elif action == '3':
            break


def weights_and_measures_converter():
    answer = input("Что будем конвертировать 'м' масса или 'р' расстояние: ")
    if answer == 'м':
        convert_for_weight()
    if answer == 'р':
        convert_for_distance()


def strong_password(password):
    if len(password) < 10:
        return False

    upper_count = 0
    lower_count = 0
    digit_count = 0

    for l in password:
        if l.isupper():
            upper_count += 1
        if l.islower():
            lower_count += 1
        if l.isdigit():
            digit_count += 1

    if upper_count == 0:
        return False
    if lower_count == 0:
        return False
    if digit_count == 0:
        return False
    return True

    upper_count = 0
    lower_count = 0
    digit_count = 0

    for l in password:
        if l.isupper():
            upper_count += 1
        if l.islower():
            lower_count += 1
        if l.isdigit():
            digit_count += 1

    if upper_count == 0:
        return False
    if lower_count == 0:
        return False
    if digit_count == 0:
        return False
    return True




def main():
    while True:
        print('Главное меню')
        print('1. Калькулятор')
        print('2. Конвертер мер и весов')
        print('3. решение уравнения дискриминантом')
        print('4. перевод из различных систем счисления в десятичную.')
        print('5. заметки')
        print('6. Надёжный пароль')
        print('7. выход из программы')

        menu_item = ''
        while menu_item not in ('1', '2', '3', '4', '5', '6', '7'):
            menu_item = input('Выберете пункт меню: ')

        if menu_item == '1':
            calculate()
        if menu_item == '2':
            weights_and_measures_converter()
        if menu_item == '3':
            decision()
        if menu_item == '4':
            a = input('Введите число: ')
            b = input('Введите разрядность: ')
            print(int(a, int(b)))
        if menu_item == '5':
            manage_notes()
        if menu_item == '6':
            strong_password(password=input('введите пароль:'))
        if menu_item == '7':
            break

if __name__ == '__main__':
    main()
