import random
import sys


words = ["bathtub", "reproduction", "department", "corner", "chorus", "temperature", "count", "notebook", "profile", "determine", "listen",
         "arrogant", "motorcycle", "central", "software", "public", "impact", "intensify", "disappointment", "light",
         "supercalifragilisticexpialidocious", "active", "comment", "customer" "participate", "brainstorm", "reason", "auction", "tournament"]
randomWord = random.choice(words)

def word_displayed(randomWord, letters_guessed):
    display = ''
    for letter in randomWord:
        if letter in letters_guessed:
            display += letter
        else:
            display += '_'
    return display

def game():
    word = randomWord
    guesses = 6
    letters_guessed = []

    print("————————————————————————————")
    print("Welcome To Guess The Word!")
    print("Guess a letter you think could be in the word below.", end = " ")
    print("You have 6 guesses left.")

    while guesses > 0:
        print(word_displayed(randomWord, letters_guessed))
        guess = input('Guess a letter: ')

        if not guess.isalpha():
            print("————————————————————————————")
            print("That's not a letter. (You cannot enter words, numbers, or special characters)")
        elif guess.isalpha():
            if guess in letters_guessed:
                print("————————————————————————————")
                print("You have already guessed that letter.")
            else:
                print("————————————————————————————")
                letters_guessed.append(guess)
                print("Letters guessed: ", letters_guessed)
                if guess not in word:
                    guesses -= 1
                    print("Incorrect Guess.", end= ' ')
                    print("You have", guesses, "guesses left.")
                elif guess in word:
                    print("You have ", guesses, " guesses left.")

        if all(letter in letters_guessed for letter in word):
            print("Congratulations, you won!")
            break



    if guesses == 0:
        print("————————————————————————————")
        print("Game Over. You Lost. The word was:", word)

game()