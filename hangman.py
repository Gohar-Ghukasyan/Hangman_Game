# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in letters_guessed:
        if i not in secret_word:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    count = 0
    blank = ['_ '] * len(secret_word)

    for i, c in enumerate(secret_word):
        if c in letters_guessed:
            count += 1
            blank.insert(count - 1, c)
            blank.pop(count)
            if count == len(secret_word):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count - 1, '_')
            blank.pop(count)
            if count == len(secret_word):
                return ''.join(str(e) for e in blank)


def get_available_letters(letters_guessed):
    s = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            s += i
    return s


def hangman(secret_word):
    g_count = 6
    guessed = False
    a_letters = string.ascii_lowercase
    arr = []
    letter = ['a', 'e', 'i', 'o', 'u']
    warning = 3
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    while g_count > 0 and guessed == False:
        if secret_word == get_guessed_word(secret_word, arr):
            guessed = True
            break
        print(f"You have {warning} warnings left.")
        print(f"You have {g_count} guesses left.")
        print(f"Available letters: {a_letters}")
        i = str(input("Please guesses a letter: ")).lower()
        if i.isalpha() and i not in a_letters:
            if warning > 0:
                if i in letter:
                    warning -= 1
                print(
                    f"The letter already used, please enter another letter. You have {warning} warnings left: {get_guessed_word(secret_word, arr)}")
                print("-" * 30)
                continue
            else:
                g_count -= 1

        arr.append(i)
        if i in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, arr)}")
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, arr)}")
            if i in letter:
                g_count -= 2
            else:
                g_count -= 1
        a_letters = get_available_letters(arr)
        print("-" * 30)

        if g_count == 0:
            print("Game over!")
            print(secret_word)

    if guessed:
        print("Congratulations, you won!")
        print(f"Your total score for this game is:{g_count * len(set(secret_word))}")


# -----------------------------------


def match_with_gaps(my_word, other_word):
    for i in range(len(my_word)):
        if my_word[i] == "_":
            continue
        if my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    arr = []
    for i in wordlist:
        if len(i) == len(my_word) and match_with_gaps(my_word, i):
            arr.append(i)
    return arr


def hangman_with_hints(secret_word):
    g_count = 6
    guessed = False
    a_letters = string.ascii_lowercase
    arr = []
    letter = ['a', 'e', 'i', 'o', 'u']
    warning = 3
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    while g_count > 0 and guessed == False:
        if secret_word == get_guessed_word(secret_word, arr):
            guessed = True
            break
        print(f"You have {warning} warnings left.")
        print(f"You have {g_count} guesses left.")
        print(f"Available letters: {a_letters}")
        i = str(input("Please guesses a letter: ")).lower()
        if i == "*":
            ls = show_possible_matches(get_guessed_word(secret_word, arr))
            print(f"Possible word matches are: {ls}")
            print("-" * 30)
            continue
        if i.isalpha() and i not in a_letters:
            if warning > 0:
                if i in letter:
                    warning -= 1
                print(
                    f"The letter already used, please enter another letter. You have {warning} warnings left: {get_guessed_word(secret_word, arr)}")
                print("-" * 30)
                continue
            else:
                g_count -= 1

        arr.append(i)
        if i in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, arr)}")
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, arr)}")
            if i in letter:
                g_count -= 2
            else:
                g_count -= 1
        a_letters = get_available_letters(arr)
        print("-" * 30)

        if g_count == 0:
            print("Game over!")
            print(secret_word)

    if guessed:
        print("Congratulations, you won!")
        print(f"Your total score for this game is:{g_count * len(set(secret_word))}")


if __name__ == "__main__":

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
