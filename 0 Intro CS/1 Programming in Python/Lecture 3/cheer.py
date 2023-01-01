from os import system as sys
sys("cls")

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
#     c = word[i]
#     if c in an_letters:
#         print("Give me an " + c + "! " + c)
#     else:
#         print("Give me a " + c + "! " + c)
#     i += 1

for c in word:
    if c in an_letters:
        print("Give me an " + c + "! " + c)
    else:
        print("Give me a " + c + "! " + c)

print("What does that spell?")

# for i in range(times):
#     print(word, "!!!")

print((word + " !!!\n")*times)
