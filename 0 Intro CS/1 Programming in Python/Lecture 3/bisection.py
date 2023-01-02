from os import system as sys
sys("cls")

# allow negative cubes
cube = float(input("cube : "))

low = 0
high = cube

# accuracy
epsilon = 0.1

guess = (high + low) / 2

num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess

    guess = (high + low) / 2

    num_guesses += 1

print(f"num_guesses : {num_guesses}")
print(f"{guess} is close to the cube root of {cube}")
