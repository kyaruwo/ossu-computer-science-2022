from os import system as sys
sys("cls")


x = int(input("square : "))
ax = abs(x)

for sqrt in range(ax+1):
    if sqrt**2 == ax:
        break

if sqrt**2 != ax:
    print(f"{x} is not a perfect square")
else:
    # imaginary number
    if x != ax:
        sqrt = str(sqrt)+"i"
    print(f"square root of {x} is {sqrt}")
