from os import system as sys
sys("cls")


cube = int(input("cube : "))
acube = abs(cube)

# accuracy, machine epsilon
epsilon = 0.1
increment = 0.01

guess = 0

num_guesses = 0
while abs(guess**3 - acube) >= epsilon and guess**3 <= acube:
    guess += increment
    num_guesses += 1

print(f"num_guesses : {num_guesses}")

if abs(guess**3 - acube) >= epsilon:
    print(f"Failed on cube root of {cube}")
else:
    # imaginary number
    if cube != acube:
        guess = str(guess)+"i"
    print(f"{guess} is close to the cube root of {cube}")
