from os import system as sys
sys("cls")


class Fraction(object):
    def __init__(self, numerator, denominator):
        Fraction.__isValid(numerator, denominator)
        self.num = numerator
        self.denom = denominator

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bot = self.denom*other.denom
        fraction = Fraction.__simplify(top, bot)
        return fraction

    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bot = self.denom*other.denom
        fraction = Fraction.__simplify(top, bot)
        return fraction

    def __float__(self):
        return self.num/self.denom

    # methods

    # methods are public by default
    def inverse(self):
        return Fraction(self.denom, self.num)

    # by adding two underscore (__) the method becomes private
    def __simplify(top, bot):
        while top % 2 == 0 and bot % 2 == 0:
            top //= 2
            bot //= 2
        return Fraction(top, bot)

    def __isValid(num, denom):
        assert type(num) == int, "integer only"
        assert type(denom) == int, "integer only"


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)


print(f"f1 = {f1}")
print(f"f2 = {f2}\n")

fsum = f1+f2
fdif = f1-f2

print(f"{f1} + {f2} = {fsum} or {float(fsum)}")
print(f"{f1} - {f2} = {fdif} or {float(fdif)}\n")

f1i = f1.inverse()
f2i = f2.inverse()

print(f"f1 inverse : {f1i} or {float(f1i)}")
print(f"f2 inverse : {f2i} or {float(f2i)}\n")


try:
    prod = f1*f2
except TypeError:
    print("Fraction * Fraction is undefine")

try:
    quo = f1/f2
except TypeError:
    print("Fraction / Fraction is undefine")

try:
    c = Fraction(420.69, 69.420)
except AssertionError:
    print("integer only")
