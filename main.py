import random

with open("words.txt","r") as file:
    contents = file.read()
    words = contents.split()
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
    guesses = 4
    letters_guessed = []

    print("Welcome To Guess The Word!")
    print("You have 4 guesses left.")

    while guesses > 0:
        print(word_displayed(randomWord, letters_guessed))
        guess = input("Guess a letter: ")
        letters_guessed.append(guess)
        print("Letters guessed: ", letters_guessed)


        if not guess.isalpha():
            print("————————————————————————————")
            print("That's not a letter. (You cannot enter whole words")


game()

