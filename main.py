import random

with open("words.txt","r") as file:
    contents = file.read()
    words = contents.split()
    randomWord = random.choice(words)
def word_displayed(randomWord, letters_guessed):
    word_displayed = ""
    for letter in randomWord:
        if letter in letters_guessed:
            word_displayed += letter
        else:
            word_displayed += "_"
    return word_displayed

def game():
    word = randomWord
    guesses = 4
    letters_gussed = []

    print("Welcome To Guess The Word!")

    while guesses > 0:
        print(word_displayed(randomWord, letters_gussed))
        guess = input("Guess a letter or a word: ")

        if not guess.isalpha():
            print("————————————————————————————")
            print("That's not a letter or word.")



game()

