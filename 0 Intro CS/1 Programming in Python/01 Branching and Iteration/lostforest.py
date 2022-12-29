from os import system as sys


def wall():
    wall_length = 26
    print("-"*wall_length+"\n"+"-"*wall_length)


while True:
    sys("cls")
    print("You are in the Lost Forest.")
    wall()
    print(">_<")
    wall()
    direction = input("Go left or right ? ")
    if direction == "left":
        break

sys("cls")
print("\n\n\n>_<\n\n")
print("You got out of the Lost Forest!")
