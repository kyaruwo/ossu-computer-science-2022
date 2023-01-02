from os import system as sys
sys("cls")


cube = int(input("cube : "))
acube = abs(cube)

num_guesses = 0
for guess in range(acube+1):
    if guess**3 >= acube:
        break
        # if guess is greater than cube, stop not a perfect cube
        # any following guess is greater than the cube itself
        #
        # if guess is equal to cube, we found the cuberoot
    num_guesses += 1

print(f"num_guesses : {num_guesses}")

if guess**3 != acube:
    print(f"{cube} is not a perfect cube")
else:
    if cube != acube:
        guess = -guess
    print(f"cube root of {cube} is {guess}")
