# print([x for x in range(int(input())+ 1) if x % 2 == 1])

# a = input().split()
# b = input().split()
# c = []
# for i in range(len(a)):
#     c.append(str(int(a[i]) - int(b[i])))
# print(' '.join(c))

# s = input().split()
# sum = 0
# for i in range(len(s)):
#     sum += int(s[i])
# print(' + '.join(s), '=', sum)

# amount = 0
# s = input().split()
# print(f'Длина самого короткого слова: {len(min(s, key=len))}')
# print(f'Длина самого длинного слова: {len(max(s, key=len))}')
# for word in s:
#     amount += len(word)
# print(f'Среднее значение длины слов: {amount / len(s)}')

# s = input().split()
# answer = []
# for word in s:
#     if len(word) == 1:
#         answer.append(word * 2)
#     else:
#         list_word=list(word)
#         list_word[0], list_word[-1] = list_word[-1], list_word[0]
#         answer.append(''.join(list_word))
# print(' '.join(answer))
