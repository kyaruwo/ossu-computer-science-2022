import time
from timeit import timeit


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


s = time.time()
print("\nfib(34) :", fib(34))
e = time.time()
print(f"time taken: {e-s}")


def fib_efficient(x):
    if x < 0:
        return

    d = {0: 1, 1: 1, 2: 2}

    def fib(n, d):
        if n in d:
            return d[n]
        else:
            ans = fib(n-1, d) + fib(n-2, d)
            d[n] = ans
            return ans
    return fib(x, d)


print("\nfib_efficient(34) :", fib_efficient(34))
print(f"time taken: {timeit(lambda: fib_efficient(34), number=1)}")
