#GuessTheWord

import random

#opens the words txt and reads it. Splitlines creates strings based on the breaks of each thing
with open("Words.txt") as w:
    word_list = w.read().splitlines()

random_number = random.randint(0, len(word_list)-1)
wordchoice = word_list[random_number]
def GetWord(word):
    return 0




