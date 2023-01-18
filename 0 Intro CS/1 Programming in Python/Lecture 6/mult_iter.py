def mult_iter(a, b):
    res = 0
    while b > 0:
        res += a
        b -= 1
    return res


print(mult_iter(4, 4))


# def recursive_mult_iter(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + recursive_mult_iter(a, b - 1)
#
# by me
def recursive_mult_iter(a, b):
    if b > 0:
        return a + recursive_mult_iter(a, b - 1)
    else:
        return 0


print(recursive_mult_iter(4, 4))
