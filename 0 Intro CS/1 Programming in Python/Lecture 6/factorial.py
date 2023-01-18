# def recursive_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*recursive_factorial(n-1)
# by me
def recursive_factorial(x):
    if x == 1:
        return 1
    elif x > 1:
        return x * recursive_factorial(x-1)
    else:
        return "infinity"


print(recursive_factorial(4))
