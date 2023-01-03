from os import system as sys


def wall():
    wall_length = 26
    print("*"*wall_length+"\n"+"*"*wall_length)


move_count = 0
while True:
    sys("cls")
    print("You are in the Lost Forest.")

    if move_count > 1:
        print("*"*26)
        print("****          ************")
        print("(╯°□°）╯︵ ┻━┻")
    elif move_count == 1:
        wall()
        print("(* ￣︿￣)")
    else:
        wall()
        print("(￣︶￣)")

    wall()
    direction = input("Go left or nah ? ")
    move_count += 1

    if direction == "left":
        break

sys("cls")
print("\n\n\n(￣︶￣)\n\n")
print(f"You got out of the Lost Forest! in {move_count} move")
