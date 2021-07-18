import math

a = math.factorial
print(a(5))


def fibb(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibb(x - 1) + fibb(x - 2)


print(fibb(5))

# def fibb(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibb(n - 1) + fibb(n - 2)
#
#
# print(fibb(10))
