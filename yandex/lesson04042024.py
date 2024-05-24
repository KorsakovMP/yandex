#
# print(len(numbers))
# print(numbers[::-1])
# print(numbers[1:-1])

# n = int(input())
# words = []
# for i in range(n):
#     word = input()
#     if word[0].lower() in 'аеёиоуыэюя':
#         words.append(word)
# print(words)

# n = int(input())
# numbers = []
# for _ in range(n):
#     num = input()
#     if '0' in num:
#         numbers.append(int(num))
# print(numbers)

# seasons = []
# seasons.append('зима')
# seasons.append('весна')
# seasons.append('лето')
# seasons.append('осень')
# print(seasons)

# n = int(input())
# numbers = list()
# for _ in range(n):
#     num = int(input())
#     numbers.append(f'{num ** 3} + {num ** 2} + {num} = {num ** 3 + num ** 2 + num}')
# print(numbers)

# n, people = int(input()), []
# for _ in range(n):
#     people.append(input())
#     people.append(input())
#     people.append(int(input()))
# print(people)

# dividers = []
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         dividers.append(i)
# print(dividers)

# n = int(input())
# words = []
# for i in range(n):
#     words.append(input())
# k = int(input())
# del words[k]
# print(words)

# n = int(input())
# answer = []
# for i in range(n):
#     num = int(input())
#     answer.append(num % 2)
# print(answer)

# n = int(input())
# letters = []
# for _ in range(n):
#     word = input().lower()
#     for letter in word:
#         if letter not in letters:
#             letters.append(letter)
# print(letters)

# n, numbers = int(input()), []
# for _ in range(n):
#     num = int(input())
#     numbers.append(int(str(num) * 3))
#     numbers.append(num * 3)
# print(numbers)

# print([for word in range(int(input()) if len(word = input()) == 5])

# palindromes = [i for i in range(1000, 10000) if list(str(i)) == list(str(i))[::-1]]
# print(palindromes)

# print(' '.join([word for word in input().split() if word.lower() != 'ну' and word.lower() != 'короче' and word.lower() != 'типа']))

# numbers = [int(input()) for _ in range(int(input()))]
# answer = [str(num) for num in numbers if num % 2 == 0 and num % 4 != 0]
# print(' '.join(answer))

# n = int(input())
# group1, group2, group3 = [], [], []
# for _ in range(n):
#     counter1 = 0
#     counter2 = 0
#     word = input()
#     for letter in word:
#         if letter.lower() in 'аеёиоуыэюя':
#             counter1 += 1
#         else:
#             counter2 += 1
#     if counter1 > counter2:
#         group1.append(word)
#     elif counter1 < counter2:
#         group2.append(word)
#     else:
#         group3.append(word)
# print('Гласных больше, чем согласных:', group1)
# print('Согласных больше, чем гласных:', group2)
# print('Гласных и согласных поровну:', group3)

# n = int(input())
# even_numbers = []
# odd_numbers = []
# for i in range(1, n + 1):
#     num = int(input())
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
# print('Чётные:', even_numbers)
# print('Нечётные:', odd_numbers)

# text6 = 'Dear David,'.split()
# text1 = 'I hope this email finds you well. I wanted to thank you for your warm welcome and hospitality during my stay. It was an unforgettable experience and I truly enjoyed my time with you and your family'.split()
# text2 = "Thank you for everything during my stay, it was great. Loved the room and  David's mom's cooking. Will try the recipes and share with my family. Appreciate showing me the city's famous sights. ".split()
# text3 = "Our evening movie viewings greatly improved my English. I now even understand what is the Englishman talking about".split()
# text4 = "I appreciate your generosity and hospitality. Hopefully, we can stay in touch and maybe you could visit us someday.".split()
# text5 = "Best regards Ann".split()
# essay = len(text1) + len(text2) + len(text3) + len(text4) + len(text5) + len(text6)
# print(essay)




