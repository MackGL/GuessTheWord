import random
import sys

words = ["angel", "judgmemt", "department", "corner", "powder", "ditch", "count", "notebook", "profile", "accent", "witch",
         "courtship", "grave", "central", "sticky", "unfair", "impact", "intensify", "budge", "light",
         "supercalifragilisticexpialidocious"]
random.shuffle(words)
randomWord = random.choice(words)

#with open("words.txt","r") as file:
    #contents = file.read()
    #words = contents.split()
    #randomWord = random.choice(words)

def word_displayed(randomWord, letters_guessed):
    display = ''
    for letter in randomWord:
        if letter in letters_guessed:
            display += letter
        else:
            display += '_'
    return display

def game():
    random.shuffle(words)
    word = randomWord
    guesses = 6
    letters_guessed = []

    #welcomes the user
    print("————————————————————————————")
    print("Welcome To Guess The Word!")
    print("Guess a letter you think could be in the word below.", end = " ")
    print("You have 4 guesses left.")

    #allows the player to input a letter, and displays word
    while guesses > 0:
        print(word_displayed(randomWord, letters_guessed))
        guess = input('Guess a letter: ')

        #restricts guess to only a letter
        if not guess.isalpha():
            print("————————————————————————————")
            print("That's not a letter. (You cannot enter words, numbers, or special characters)")
        else:
            #stops letter repeats in letter_guessed
            if guess in letters_guessed:
                print("————————————————————————————")
                print("You have already guessed that letter.")
                guesses += 1
            #puts letter guessed in letters_guessed list
            else:
                print("————————————————————————————")
                letters_guessed.append(guess)
                print("Letters guessed: ", letters_guessed)

                #displays number of guesses left
            if guess in word:
                print("You have ", guesses, " guesses left.")
                #subtracts guess when answer is wrong
            elif guess not in word:
                guesses -= 1
                print("Incorrect Guess.", end= ' ')
                print("You have", guesses, "guesses left.")

        if all(letter in letters_guessed for letter in word):
            print("Congratulations, you won!")
            restart = input("Would you like to play again? (Enter yes or no): ")
            if restart == "yes":
                print(randomWord)
                game()
            elif restart == "no":
                quit("You quite the game.")




    if guesses == 0:
        print("————————————————————————————")
        print("Game Over. You Lost. The word was:", word)


game()