import numpy as np
from os import system
def clear(): system("cls")


x = y = p = None

clear()
while True:

    try:
        x = int(input("Enter number x: "))
        y = int(input("Enter number y: "))
        p = x**y
        break
    except:
        clear()
        continue

xlog2i = int(np.log2(x))
xlog2f = np.log2(x)

if xlog2i == xlog2f:
    xlog2 = xlog2i
else:
    xlog2 = xlog2f

print(f"x**y = {p}")
print(f"log2(x) = {xlog2}")
