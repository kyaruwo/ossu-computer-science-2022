from os import system as sys
sys("cls")

# allow negative cubes
cube = float(input("cube : "))

# accuracy
epsilon = 0.1
increment = 0.01

guess = 0
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1

print(f"num_guesses : {num_guesses}")
if abs(guess**3 - cube) >= epsilon:
    print(f"Failed on cube root of {cube}")
else:
    print(f"{guess} is close to the cube root of {cube}")
