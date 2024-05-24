#
# n = int(input())#считываем с клавиатуры n
# for i in range(1, n + 1):# цикл от 1 (не от 0) до n+1
#     print(str(i) * i)#преобразуем i в строку и строку умножаем на int

# n = int(input())#считываем с клавиатуры n
# count = 0#создаем переменнкю счетчик
# while n != 0:#создаем цикл while
#     n, remains = divmod(n, 10)#находим остаток от деления и сохраняем в переменой remains
#     #если n = 6543 то после divmod n =654, а remains = 3
#     if remains % 2 == 1:#проверяем число на четность
#         count += remains#добавляем значение в щетчик
# print(count)#выводим щетчик

# count = 0#создаем счетчик
# max_n = -101#по условию задачи числа вводятся не больше ста по модулю
# n = int(input())#считываем с клавиатуры n
# if n % 2 == 0:#я хотел первое значение n сразу сохранить как максимальное для этого один запуск я вынес из цикла, а цикл уменшил с 5 до 4
#     count += 1#но если первое число было нечетное решение не проходило тесты
#     max_n = n
# for i in range(4):#создаем цикл
#     n = int(input())#считываем n
#     if n % 2 == 0:#проверяю четность
#         count += 1#увеличиваю считчик на 1
#         max_n = max(max_n, n)#в функцию передаем максимальное значение и текущее, а возвращает большее из них
# if count != 0:#если все введеные числа нечетные значение счетчика не изменитсяи останется равным 0
#     print(count)#выводим количество четных чисел
#     print(max_n)#выводим максимльное четное число
# else:
#     print('Нет')#если все введеные числа нечетные выводим нет

# count = 0
# max_n = -1001
# n = int(input())
# if n % 3 == 0:
#     count += 1
#     max_n = n
# for i in range(6):
#     n = int(input())
#     if n % 3 == 0:
#         count += 1
#         max_n = max(max_n, n)
# if count != 0:
#     print(count)
#     print(max_n)
# else:
#     print('Нет')

# n = int(input())#считываем с клавиатуры n
# # remains = 0 #програма упала на тестах при n = 100 так как цикл не разу не выполнился. можно было поменять условие на
# # n > 99 или n >= 100. но этот вариант я придумал после завершение теста.
# while n >= 100:#выполняем цикл пока n больше 100
#     n, remains = divmod(n, 10)#выполняем деление с остатком n на 10 если n = 6543 то после divmod n =654, а remains = 3
# print(n, remains)#так как цикл завершился n < 100 то в остатке будет третья цифра из введенего числа

# print(divmod(10, 3))
# print(10// 3, 10 % 3)

# while True:
#     text = input()
#     if text == 'стоп':
#         break
#     print(text)
#
#
# text = input()
# while text != 'стоп':
#     print(text)
#     text = input()

# n = int(input())
# for i in range(1, n +1):
#     print(str(i)* n)


# for i in range(1, 9):
#     print(i + 1)


# for i in range(1, 9):
#     print(i)

# count = 0
# count1 = 0
# count2 = 0
# for i in range(5):
#     n = int(input())
#     if n > 0:
#         count += 1
#     if n < 0:
#         count1 += 1
#     if n == 0:
#         count2 += 1
# print(f'Положительных:  {count}')
# print(f'Отрицательных:  {count1}')
# print(f'Равных нулю:  {count2}')

# n = int(input())
# for i in range(n):
#     n = int(input())
# n = 5
# for i in range(n * 2):
#     if i % 2 == 1:
#         print(str(i) * i)

# n = int(input())
# count = 0
# for i in range(n):
#     count += int(input())
# print(f'Общая сумма = {count}')

# counter = 0
# m = int(input())
# n = int(input())
# for i in range(m, n):
#     if (i ** 3) % 10 in (1, 9):
#         counter += 1
# print(counter)

# counter = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += 1
# print(counter)

# a = int(input())
# b = int(input())
# # здесь нужно обменять значения переменных
# print(b)
# print(a)

# flag = 'Да'
# for i in range(5):
#     n = int(input())
#     if n % 2 == 1:
#         flag = 'да'
#     else:
#         flag = 'нет'
# print(flag)

# total = 0
# n = int(input())
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)

# n = int(input())
# a, b = 1, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# n = int(input())
# flag = True
# for i in range(2, n):
#     if n % i == 0:
#         flag = False
#         break
# if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# for i in range(1, 101):
#     # if i != 25 and i != 50 and i !=75:
#     if i not in (25, 50, 75):
#         print(i)

# n = int(input())
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(1, i+1):
#         if i % j == 0:
#             print('+', end='')
#     print()

# n = int(input())
# total = 0
# while n >= 10:
#     total = 0
#     while n > 0:
#         n, remains = divmod(n, 10)
#         total += remains
#     n = total
# print(total)

# n = 3
# count = 0
# for i in range(1, n + 1):
#     for j in range(i):
#         count += 1
#         print(count, end=' ')
#     print()
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for j in range(1, i):
#         print(i - j, end='')
#     print()
