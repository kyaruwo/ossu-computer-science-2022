# vscode my beloved
try:
    import os
    def clear(): os.system("cls")
    clear()
    os.chdir("0 Intro CS/1 Programming in Python/Lecture 4/Pset2")
except:
    pass


# Problem Set 2, hangman.py
# Name: kyaruwo
# Collaborators: me
# Time spent: 2023/01/05 - 2023/01/??

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    os.system("pause")
    clear()
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word:
        if c not in letters_guessed:
            return False
    else:
        return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for c in secret_word:
        if c not in letters_guessed:
            guessed_word += "_ "
        else:
            guessed_word += c+" "
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = string.ascii_lowercase
    for c in letters_guessed:
        available_letters = available_letters.replace(c, "")
    return available_letters


#


def is_letter_valid(letter, letters_guessed, swl):
    if letter not in string.ascii_lowercase or letter == "":
        print(f"Oops! That is not a valid letter. {swl}")
        return False
    if letter in letters_guessed:
        print(f"Oops! You've already guessed that letter. {swl}")
        return False
    return True


def get_swl(guessed_word, warnings_left):
    if warnings_left > 0:
        return f"You have {warnings_left-1} warnings left: {guessed_word}"
    else:
        return f"You have no warnings left\nso you lose one guess: {guessed_word}"


#


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    warnings_left = 3
    guesses_remaining = 6
    letters_guessed = ""

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_left} warnings left.")

    while True:
        print("-"*48)

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print(
                f"Your total score for this game is: {guesses_remaining*len(set(secret_word))}")
            break
        if guesses_remaining < 1:
            print(
                f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break

        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter = input("Please guess a letter: ").lower()

        clear()

        swl = get_swl(get_guessed_word(secret_word, letters_guessed),
                      warnings_left)

        if not is_letter_valid(letter, letters_guessed, swl):
            warnings_left -= 1
            if warnings_left < 0:
                guesses_remaining -= 1
            continue

        letters_guessed += letter
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if letter in secret_word:
            print(f"Good guess: {guessed_word}")
        else:
            print(f"Oops! That letter is not in my word: {guessed_word}")
            if letter in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] == "_":
            if other_word[i] in my_word:
                return False
            continue

        if my_word[i] != other_word[i]:
            return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    matchlist = ""
    for word in wordlist:  # optimize using bisection search
        if match_with_gaps(my_word, word):
            matchlist += word+" "

    if len(matchlist) != 0:
        return ("\n"+matchlist)

    return "No matches found"


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_left = 3
    guesses_remaining = 6
    letters_guessed = ""

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_left} warnings left.")

    while True:
        print("-"*48)

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print(
                f"Your total score for this game is: {guesses_remaining*len(set(secret_word))}")
            break
        if guesses_remaining < 1:
            print(
                f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break

        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter = input("Please guess a letter: ").lower()

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        clear()

        if letter == "*":
            print("Possible word matches are : " +
                  show_possible_matches(guessed_word))
            print(f"guess : {guessed_word}")
            continue

        swl = get_swl(guessed_word, warnings_left)
        if not is_letter_valid(letter, letters_guessed, swl):
            warnings_left -= 1
            if warnings_left < 0:
                guesses_remaining -= 1
            continue

        letters_guessed += letter
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if letter in secret_word:
            print(f"Good guess: {guessed_word}")
        else:
            print(f"Oops! That letter is not in my word: {guessed_word}")
            if letter in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # temp
    # hangman("tact")
    # hangman("else")

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    # temp
    # hangman_with_hints("tact")
    # hangman_with_hints("else")
    # hangman_with_hints("apple")
