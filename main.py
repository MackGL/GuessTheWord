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
    print("You have 4 guesses left.", end = " ")
    print("Enter a letter!")

    while guesses > 0:
        print(word_displayed(randomWord, letters_guessed))
        guess = input("Guess a letter: ")

        if not guess.isalpha():
            print("————————————————————————————")
            print("That's not a letter. (You cannot enter words, numbers, or special characters)")
        else:
            if guess in letters_guessed:
                return
            elif guess not in letters_guessed:
                letters_guessed.append(guess)
            print("Letters guessed: ", letters_guessed)
            if guess in word:
                print("You have ", guesses, " guesses left.")
            else:
                guesses -= 1
                print("You have ", guesses, "guesses left.")





    if guesses == 0:
        print("Game Over. You Lost.")



game()

