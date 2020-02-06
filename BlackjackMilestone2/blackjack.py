'''
Blackjack - Milestone project 2
'''

import random
import time

cardsuits = ["Diamonds","Clubs","Spades","Hearts"]
cardnumbers = ["2","3","4","5","6","7","8","9","T","J","K","Q","A"]
cardvalues = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10,"A":11,"a":1}

class Card:

    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        self.value = cardvalues[number]
    
    def __str__(self):
        return(self.number + " of " + self.suit)

class Deck:

    def __init__(self):
        self.deck = []
        for suit in cardsuits:
            for num in cardnumbers:
                self.deck.append(Card(suit,num))
    
    def initlength(self):
        self.length = len(self.deck)
    
    def printdeck(self):
        counter = 0
        while counter < len(self.deck):
            print(str(self.deck[counter]))
            counter = counter+1
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return(self.deck.pop(0))

    def refill(self):
        for suit in cardsuits:
            for num in cardnumbers:
                self.deck.append(Card(suit,num))

class Bankroll:

    def __init__(self,owner,amount):
        self.owner = owner
        self.amount = amount

    def deposit(self,depamount):
        self.amount = self.amount+depamount
        print("Deposited {}".format(depamount))
        print("New balance is {}".format(self.amount))
    
    def bet(self,betamount):
        if self.amount < betamount:
            print("Not enough funds")
        else:
            self.amount = self.amount-betamount
            print("bet {} from bankroll".format(betamount))
    
    def inquiry(self):
        return(self.amount)

class Hand:

    def __init__ (self):
        self.cards = []
        self.cardnums = []
        self.value = 0
        self.aces = 0

    def printhand (self):
        counter = 0
        while counter < len(self.cards):
            print(str(self.cards[counter]))
            counter = counter+1

    def addcard (self,card):
        self.cards.append(card)
        self.cardnums.append(card.number)
        self.value = self.value + card.value

    def resethand (self):
        self.cards.clear()
    
    def getcard (self,index):
        return self.cards[index]

    def cardsinhand (self):
        return len(self.cards)
    
    def adjustforace (self):
        #print("Called A for A function")
        if "A" in self.cardnums:
            #print("Found A in list")
            if self.value > 21:
                #print("Noticed ur value OwO What's this? *bolgy wolgy nuzzles*")
                self.value = self.value-10
                for item in self.cardnums:
                    if item == "A":
                        #print("Replaced A with a")
                        item = "a"
                        break

    
    def printcards (self):
        line1 = "+-----+ "
        line2 = "|{}    | "
        line3 = "|  {}  | "
        line4 = "|    {}| "
        line5 = "+-----+ "
        printline1 = ""
        printline2 = ""
        printline3 = ""
        printline4 = ""
        printline5 = ""

        counter = 0
        for item in self.cards:
            printline1 = printline1 + line1
            printline2 = printline2 + line2.format(self.cards[counter].number)
            printline3 = printline3 + line3.format((self.cards[counter].suit)[0])
            printline4 = printline4 + line4.format(self.cards[counter].number)
            printline5 = printline5 + line5
            counter = counter + 1
        
        print(printline1)
        print(printline2)
        print(printline3)
        print(printline4)
        print(printline5)
    
    def hidefirst (self):
        line1 = "+-----+ "
        line2 = "|{}    | "
        line3 = "|  {}  | "
        line4 = "|    {}| "
        line5 = "+-----+ "
        printline1 = "+-----+ "
        printline2 = "|XXXXX| "
        printline3 = "|XXXXX| "
        printline4 = "|XXXXX| "
        printline5 = "+-----+ "

        counter = 1
        while counter < (len(self.cards)):
            printline1 = printline1 + line1
            printline2 = printline2 + line2.format(self.cards[counter].number)
            printline3 = printline3 + line3.format((self.cards[counter].suit)[0])
            printline4 = printline4 + line4.format(self.cards[counter].number)
            printline5 = printline5 + line5
            counter = counter + 1
        
        print(printline1)
        print(printline2)
        print(printline3)
        print(printline4)
        print(printline5)


def clear_screen():
    counter = 0
    while counter < 100:
        print("")
        counter = counter + 1

def deal_card(whathand):
    cardchange = deck.deal()
    whathand.addcard(cardchange)

def shuffle_display(times):
    print("Shuffling Cards")
    deck.shuffle()
    time.sleep(times)
    clear_screen()
    print("Shuffling Cards.")
    deck.shuffle()
    time.sleep(times)
    clear_screen()
    print("Shuffling Cards..")
    deck.shuffle()
    time.sleep(times)
    clear_screen()
    print("Shuffling Cards...")
    time.sleep(times)
    clear_screen()

def print_table(playerhand,dealerhand,bet):
    clear_screen()
    print("Dealer shows:")
    dealerhand.hidefirst()
    print("")
    print("")
    print("")
    print("Your bet: {}".format(bet))
    print("Your cards:")
    hand.printcards()
    print("Total value:")
    print(hand.value)

def print_open_table(playerhand,dealerhand,bet):
    clear_screen()
    print("Dealer shows:")
    dealerhand.printcards()
    print(dealerhand.value)
    print("")
    print("")
    print("")
    print("Your bet: {}".format(bet))
    print("Your cards:")
    hand.printcards()
    print("Total value:")
    print(hand.value)

def player_wins(pot,playerbank):
    clear_screen()
    print("You win!")
    print("You've won {}".format(pot))
    winnings = pot * 2
    playerbank.deposit(winnings)
    print("You now have {} GoodBoiPoints!".format(playerbank.amount))
    time.sleep(2)

def dealer_wins(pot,playerbank):
    clear_screen()
    print("You lose!")
    print("You've lost {}".format(pot))
    print("You now have {} GoodBoiPoints!".format(playerbank.amount))
    time.sleep(2)

def push(pot,playerbank):
    clear_screen()
    print("Push!")
    playerbank.deposit(pot)
    print("You now have {} GoodBoiPoints!".format(playerbank.amount))
    time.sleep(2)

def player21(pot,playerbank):
    clear_screen()
    print("Player gets Blackjack!")
    playerbank.deposit(pot+pot*1.5)
    print("You now have {} GoodBoiPoints!".format(playerbank.amount))
    time.sleep(2)

#Test Code
'''
testhand = Hand()
testdeck = Deck()
testcard1 = Card("Diamonds","A")
testcard2 = Card("Diamonds","A")
testhand.addcard(testcard1)
testhand.addcard(testcard2)
testhand.printcards()
print(testhand.value)
time.sleep(3)
testhand.adjustforace()
print(testhand.value)
time.sleep(3)
'''
#ACTUAL CODE - ABOVE IS TEST

clear_screen()
print("Welcome to Blackjack!")
print("Enter your name!")
playername = input("")
clear_screen()

print("Welcome {}!".format(playername))
print("You shall start with 500 GoodBoiPoints")
playerbank = Bankroll(playername,500)
time.sleep(0.5)

game = True
while game == True:

    deck = Deck()
    shuffle_display(0.5)
    
    roundactive = True
    while roundactive == True:

        deck.initlength()
        if deck.length < 10:
            deck.refill()
            deck.shuffle()
            deck.shuffle()
            deck.shuffle()

        betcheck = False
        while betcheck == False:
            clear_screen()
            print("Your current balance is {} GoodBoiPoints".format(playerbank.amount))
            print("How much would you like to bet?")
            currentbet = input("")
            try:
                currentbet = int(currentbet)
            except:
                clear_screen()
                print("That's not a number chief")
            else:
                if currentbet > playerbank.amount:
                    clear_screen()
                    print("Sorry, you don't have enough money. You have {} GoodBoiPoints".format(playerbank.amount))
                else:
                    playerbank.bet(currentbet)
                    betcheck = True
        
        clear_screen()
        print("You have bet {} GoodBoiPoints!".format(currentbet))
        time.sleep(0.5)

        clear_screen()

        handactive = True
        again = ""
        
        dealerhand = Hand()
        hand = Hand()

        deal_card(dealerhand)
        deal_card(dealerhand)
        dealercard1 = dealerhand.getcard(0)
        dealercard2 = dealerhand.getcard(1)

        deal_card(hand)
        deal_card(hand)
        card1 = hand.getcard(0)
        card2 = hand.getcard(1)
        hand.adjustforace()

        blackjack = False

        if hand.value == 21:
            print_open_table(hand,dealerhand,currentbet)
            print("21!")
            time.sleep(2)
            player21(currentbet,playerbank)
            blackjack = True
        else:
            playerturn = True

        breakloop = False
        while blackjack == False:
            
            while playerturn == True:

                print_table(hand,dealerhand,currentbet)

                choicecheck = False
                while choicecheck == False:
                    print("")
                    print("What would you like to do? (Hit/Stay)")
                    choice = input("")
                    if choice == "Stay":
                        choicecheck = True
                    elif choice == "Hit":
                        choicecheck = True
                    else:
                        print("That wasn't an option.")
                
                if choice == "Hit":
                    deal_card(hand)
                    hand.adjustforace()
                    hand.printcards()
                    if hand.value > 21:
                        print_table(hand,dealerhand,currentbet)
                        print("You busted!")
                        time.sleep(2)
                        break
                elif hand.cardsinhand() == 5 or choice == "Stay":
                    break
            
            dealerturn = True
            while dealerturn == True:
                print_open_table(hand,dealerhand,currentbet)
                time.sleep(1)

                if dealerhand.value < 18:
                    deal_card(dealerhand)
                elif dealerhand.value > 21:
                    print("Dealer busts!")
                    time.sleep(2)
                    break
                else:
                    break
                dealerhand.adjustforace()
            
            if dealerhand.value > 21:
                if hand.value > 21:
                    dealer_wins(currentbet,playerbank)
                else:
                    player_wins(currentbet,playerbank)
            elif dealerhand.value > hand.value:
                dealer_wins(currentbet,playerbank)
            elif dealerhand.value == hand.value:
                push(currentbet,playerbank)
            else:
                if hand.value > 21:
                    dealer_wins(currentbet,playerbank)
                else:
                    player_wins(currentbet,playerbank)
            
            break
            
        clear_screen()
        while True:
            print("Play again? (Y/N)")
            again = input("")
            if again == "Y":
                breakloop = True
                break
            elif again == "N":
                breakloop = True
                break
            else:
                print("I'm sorry, that wasn't an option")
            
        if playerbank.amount == 0:
            clear_screen()
            print("You are out of money! Goodbye!")
            time.sleep(2)
            break
        elif again == "Y":
            pass
        else:
            break
    break