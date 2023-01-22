# def fib(x):
#     """
#     assumes x an int >= 0
#     returns Fibonacci of x
#     """
#     if x == 0 or 1 == x:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
#
# by me
def fib(x):
    """returns Fibonacci of x"""
    if x < 0:
        return
    elif x > 1:
        return fib(x-1) + fib(x-2)
    else:
        return 1


print(fib(0))
print(fib(1))
print(fib(4))
print(fib(-1))
