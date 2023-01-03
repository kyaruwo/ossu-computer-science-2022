from os import system as sys
sys("cls")


def is_even(x):
    """
    Return True if x is even, else False
    """
    return x % 2 == 0


print(is_even(2))
