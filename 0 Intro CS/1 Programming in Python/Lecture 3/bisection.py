from os import system as sys
sys("cls")


cube = int(input("cube : "))
acube = abs(cube)

low = 0
high = acube

# accuracy, machine epsilon
epsilon = 0.1

guess = (high + low) / 2

num_guesses = 0
while abs(guess**3 - acube) >= epsilon:
    if guess**3 < acube:
        low = guess
    else:
        high = guess

    guess = (high + low) / 2

    num_guesses += 1

print(f"num_guesses : {num_guesses}")

if cube != acube:
    guess = -guess
print(f"{guess} is close to the cube root of {cube}")
