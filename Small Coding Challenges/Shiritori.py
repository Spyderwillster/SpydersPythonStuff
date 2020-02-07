'''
Shiritori game - inspiration from edabit.com Python excersizes
https://edabit.com/challenge/dLnZLi8FjaK6qKcvv
'''

import time

class WordList:

    def __init__(self):
        self.words = ["   "]
        self.check = False
        self.counter = 0
        self.score = 0

    def check_word(self,word):
        for item in self.words:
            if item == word.lower():
                print("You already used {}".format(item))
                self.check = True
        lastword = self.words[self.counter]
        lastletter = lastword[-1]
        lastletter = lastletter.lower()
        newletter = word[0]
        newletter = newletter.lower()
        if self.counter != 0:
            if lastletter != newletter:
                print("That doesn't start with {}".format(lastletter))
                self.check = True

def clear_screen():
    for number in range(0,100):
        print("")

wordlist = WordList()

while True:
    clear_screen()
    wordlist.words = ["   "]
    wordlist.counter = 0
    wordlist.score = 0
    print("Welcome to shiritori. Type words that begin with the last letter of the last word. Do not reuse words.")
    time.sleep(2)
    wordlist.check = False
    while True:
        clear_screen()
        print("Last word: {}".format(wordlist.words[wordlist.counter]))
        print("Enter new word:")
        newWord = input("")
        wordlist.check_word(newWord)
        wordlist.words.append(newWord.lower())
        wordlist.counter += 1
        if wordlist.check == True:
            print("You have lost")
            time.sleep(2)
            break
        wordlist.score += 1
    
    clear_screen()
    print("your words were: {}".format(wordlist.words))
    print("Your score was: {}".format(wordlist.score))
    print("Play again? (Y/N)")
    again = input("")
    if again == "N":
        clear_screen()
        break

