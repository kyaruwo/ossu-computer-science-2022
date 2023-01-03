from os import system as sys
sys("cls")


def a():
    print("inside function a")


def b(y):
    print("inside function b")
    return y


def c(z):
    print("inside function c")
    return z()


# executes the function first before printing out the string

print(f"function a: {a()}\n")

print(f"function b: {40 + b(2)}\n")

print(f"function c: {c(a)}\n")
