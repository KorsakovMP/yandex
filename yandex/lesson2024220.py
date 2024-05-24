# #                   0         1     2         3       4
# food_and_drinks = ['хлеб', 'сыр', 'творог', 'сок', 'морс']
# drinks = food_and_drinks[3:]
# print(drinks)

# ['футбол', 'волейбол', 'баскетбол', 'хоккей', 'теннис', 'плавание', 'борьба', 'велоспорт', 'фехтование']
# ['футбол', 'волейбол', 'баскетбол', 'хоккей', 'теннис', 'плавание', 'пение', 'борьба', 'велоспорт', 'фехтование']
# sports = ['футбол', 'волейбол', 'баскетбол', 'хоккей', 'танцы', 'пение', 'борьба', 'велоспорт', 'фехтование']
# sports[4:6] = ['теннис', 'плавание']
# print(sports)

# food = ['хлеб', 'сыр', 'творог', 'яйца', 'рыба']
# drinks = ['сок', 'морс', 'лимонад', 'молоко', 'вода']
# food_and_drinks = food + drinks
# print(food_and_drinks)

# onetwothree = [1, 2, 3] * 3
# print(onetwothree)

# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
# print(sum(odd_numbers) / len(odd_numbers))

# numbers = [0.1, 0.3, -1.5, -1.7, 0.9, 0.11, -1.13, -1.15]
# print(f'Минимальный элемент ={min(numbers)}')
# print(f'Максимальный элемент ={max(numbers)}')

# numbers = [-15, -10, -5, 0, 5, 10, 15]
# print(numbers[::-1])

# wild_animals = ['кот', 'собака', 'волк', 'лиса', 'медведь', 'свинья', 'коза']
# wild_animals[0]= 'ёж'
# wild_animals[1]= 'заяц'
# wild_animals[5]= 'кабан'
# wild_animals[6]= 'лось'
# print(wild_animals)

# numbers = [-15, -10, -5, 0, 5, 10, 15]
# numbers[4:] = [-5, -10, -15]
# print(numbers)

# weather1 = ['солнечно', 'пасмурно']
# weather2 = ['дождь']
# weather3 = weather1 + weather2 * 5 + weather1 * 2
# print(weather3)

# n = int(input())
# print([x + 1 for x in range(n)])
# print([n] * n)
# print([x - n for x in range(n)])

l = []
for _ in range(int(input())):
    l.append(input())
print(l)
