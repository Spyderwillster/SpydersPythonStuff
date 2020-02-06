def checkwin(boardstate):
    if boardstate[0] == boardstate[1] and boardstate[1] == boardstate[2]:
        return True
    elif boardstate[3] == boardstate[4] and boardstate[4] == boardstate[5]:
        return True
    elif boardstate[6] == boardstate[7] and boardstate[7] == boardstate[8]:
        return True
    elif boardstate[0] == boardstate[3] and boardstate[3] == boardstate[6]:
        return True
    elif boardstate[1] == boardstate[4] and boardstate[4] == boardstate[7]:
        return True
    elif boardstate[2] == boardstate[5] and boardstate[5] == boardstate[8]:
        return True
    elif boardstate[0] == boardstate[4] and boardstate[4] == boardstate[8]:
        return True
    elif boardstate[6] == boardstate[4] and boardstate[4] == boardstate[2]:
        return True

def checktie(boardstate):
    opencount = 0
    for item in boardstr:
        if item in boardmarks:
            opencount = opencount+1
    if opencount == 0:
        return True

def printboard(boardstate):
    print("           ")
    print("           ")
    print("           ")
    print("           ")
    print("           ")
    print("           ")
    print("           ")
    print("           ")
    print("           ")
    print("   |   |   ")
    print(" {a} | {b} | {c} ".format(a=boardstate[6],b=boardstate[7],c=boardstate[8]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {a} | {b} | {c} ".format(a=boardstate[3],b=boardstate[4],c=boardstate[5]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {a} | {b} | {c} ".format(a=boardstate[0],b=boardstate[1],c=boardstate[2]))
    print("   |   |   ")

reset = True
while reset == True:
    print("Welcome to Tic Tac Toe")
    p1markpass = False
    while p1markpass == False:
        print("Player 1: X's or O's")
        p1mark = input("")
        if p1mark == 'X' or p1mark == 'O':
            p1markpass = True
            if p1mark == 'X':
                p2mark = 'O'
                print("Player 2 assigned to O's")
            else:
                p2mark = 'X'
                print("Player 2 assigned to X's")
        else:
            print("Please enter 'X' or 'O'")
    
    boardnum = [1,2,3,4,5,6,7,8,9]
    boardstr = ["1","2","3","4","5","6","7","8","9"]
    boardmarks = ["1","2","3","4","5","6","7","8","9"]
    currentwin = False
    currentwinner = "Nope"
    istie = False
    
    gamerun = True
    playturn = 1
    
    while gamerun == True:
        printboard(boardmarks)
        if playturn == 1:
            print("Player 1's turn")
        elif playturn == 2:
            print("Player 2's turn")
        else:
            print("How the hell did this happen? Something broke!")
        inputint = False
        while inputint == False:
            print("What available space would you like to put it in?")
            move = input("")
            if move in boardstr:
                move = int(move)
                if boardmarks[(move-1)] == "X" or boardmarks[(move-1)] == "O":
                    print("Space {} is occupado".format(move))
                else:
                    inputint = True
            elif move == "exit":
                inputint = True
                gamerun = False
                break
            else:
                print("You fool, {} isn't a valid input.".format(move))
        if playturn == 1:
            print("Placing X in space {}".format(move))
            boardmarks[(move-1)] = "X"
        elif playturn == 2:
            print("Placing O in space {}".format(move))
            boardmarks[(move-1)] = "O"
        currentwin = checkwin(boardmarks)
        istie = checktie(boardmarks)
        if istie == True:
            print("Tie game!")
            againcheck = False
            while againcheck == False:
                print("Would you like to play again? (Y/N)")
                again = input("")
                if again == "Y":
                    reset = True
                    gamerun = False
                    againcheck = True
                elif again == "N":
                    reset = False
                    gamerun = False
                    againcheck = True
                else:
                    print(again+" is not a valid input!")
        if currentwin == True:
            if playturn == 1:
                currentwinner = 1
            else:
                currentwinner = 2
            print("Congratulations! Player {} has won!".format(currentwinner))
            againcheck = False
            while againcheck == False:
                print("Would you like to play again? (Y/N)")
                again = input("")
                if again == "Y":
                    reset = True
                    gamerun = False
                    againcheck = True
                elif again == "N":
                    reset = False
                    gamerun = False
                    againcheck = True
                else:
                    print(again+" is not a valid input!")
        if playturn == 1:
            playturn = 2
        elif playturn == 2:
            playturn = 1
        else:
            print("Something went wrong.")