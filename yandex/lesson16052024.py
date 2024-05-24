# n = 12040601001
# p = 1
# for i in str(n):
#     x = int(i)
#     if x != 0:
#         p *= x
# print(p)


# def my_sum(i: int):
#     s = str(i)
#     ammount = 0
#     for i in s:
#         ammount += int(i)
#     return ammount
#
# def my_multiply(i: int):
#     s = str(i)
#     multiply = 1
#     for i in s:
#         multiply *= int(i)
#     return multiply
#
# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     i0 = i % 10
#     i1 = (i % 100 - i0) // 10
#     if i0 == 2 and my_multiply(i) > my_sum(i):
#         count += 1
#
# print(count)


s = '0012'
n = 2


def cript(s: str, n: int):
    for _ in range(n):
        s = s.replace('01', '1021102')
        s = s.replace('021', '1201')
    return s


assert len(cript('0012', 2)) == 24
assert len(cript('01211', 3)) == 31
print(len(cript(input(), int(input()))))
