'''
Pong on a Launchpad
Coded by Will Watkins using pygame
Built for Lanuchpad MKII
'''

#package imports
import pygame
import pygame.midi
import time
import random

#initializations
pygame.init()
pygame.midi.init()

#Getting MIDI ports
portOut = pygame.midi.get_default_output_id()
portIn = pygame.midi.get_default_input_id()
print("Using {a} for MIDI input and {b} for MIDI output".format(a=portIn,b=portOut))

#defining MIDI methods
midi_out = pygame.midi.Output(portOut,0)
midi_in = pygame.midi.Input(portIn,0)

#Defining number profiles so that we can print them later
num1x = [4,4,4,4,4,5,5,5,5,5]
num1y = [3,4,5,6,7,3,4,5,6,7]
num2x = [3,3,3,3,4,4,4,5,5,5,6,6,6,6]
num2y = [3,4,5,7,3,5,7,3,5,7,3,5,6,7]
num3x = [3,3,3,4,4,4,5,5,5,6,6,6,6,6]
num3y = [3,5,7,3,5,7,3,5,7,3,4,5,6,7]
num4x = [3,3,3,4,5,6,6,6,6,6]
num4y = [5,6,7,5,5,3,4,5,6,7]
num5x = [3,3,3,3,4,4,4,5,5,5,6,6,6,6]
num5y = [3,5,6,7,3,5,7,3,5,7,3,4,5,7]
num6x = [3,3,3,3,3,4,4,4,5,5,5,6,6,6,6]
num6y = [3,4,5,6,7,3,5,7,3,5,7,3,4,5,7]
num7x = [3,4,5,6,6,6,6,6]
num7y = [7,7,7,3,4,5,6,7]
num8x = [3,3,3,3,3,4,4,4,5,5,5,6,6,6,6,6]
num8y = [3,4,5,6,7,3,5,7,3,5,7,3,4,5,6,7]
num9x = [3,3,3,3,4,4,4,5,5,5,6,6,6,6,6]
num9y = [3,5,6,7,3,5,7,3,5,7,3,4,5,6,7]
num10x = [2,2,2,2,2,4,4,4,4,4,5,5,6,6,7,7,7,7,7]
num10y = [3,4,5,6,7,3,4,5,6,7,3,7,3,7,3,4,5,6,7]
numbersx = [num1x,num2x,num3x,num4x,num5x,num6x,num7x,num8x,num9x,num10x]
numbersy = [num1y,num2y,num3y,num4y,num5y,num6y,num7y,num8y,num9y,num10y]

#Defining possible player colors
gameColors = [3,5,9,13,17,21,25,29,4,8,12,16,32,45,95,100]

#Defining game objects
class Board:

    #Init Ball, creating the board coordinates
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boardx = []
        self.boardy = []
        countx = 1
        while countx <= width:
            self.boardx.append(countx)
            countx = countx + 1
        
        county = 1
        while county <= height:
            self.boardy.append(county)
            county = county+1
        print(self.boardx)
        print(self.boardy)
    
    #Sets all pixels to off
    def clear_board(self):
        for x in self.boardx:
            for y in self.boardy:
                pixel = pair_to_pixel(x,y)
                midi_out.note_off(pixel)

    #Sets a pixel to a given color
    def light_pixel(self, x, y, color):
        pixel = pair_to_pixel(x,y)
        midi_out.note_on(pixel,color)
    
    def fill_board(self,color):
        for x in self.boardx:
            for y in self.boardy:
                pixel = pair_to_pixel(x,y)
                midi_out.note_on(pixel,color)

#Creates object for housing balls
class BallBag:

    def __init__(self):
        self.balls = []
    
    def add_ball(self,objecttype,posx,posy,color):
        self.balls.append(objecttype(posx,posy,color))

#Wraps a winner class to call winner later in script
class Winner:

    def __init__(self):
        self.winner = 0
        self.iswin = False

#Ball object
class Ball:

    #Initializes ball with position, color, and random x velocity between 0 and 1
    def __init__(self,x,y,color):
        self.positionx = x
        self.positiony = y
        self.color = color
        self.velocityx = 1
        self.velocityy = 1
    
    #Shows the ball in space
    def show_ball(self, space):
        space.light_pixel(self.positionx,self.positiony,self.color)
    
    #Blanks out ball position
    def erase_ball(self, space):
        space.light_pixel(self.positionx,self.positiony,0)

    #Updates position of ball
    def update_ball(self):
        self.positionx = self.positionx + self.velocityx
        self.positiony = self.positiony + self.velocityy

#Paddle object
class Paddle:
    
    #Initialize the paddle with length and middle position
    def __init__(self,positionx,color):
        self.positionx = positionx
        self.positiony = 4
        self.color = color
        self.colorIndex = 0
        self.score = 0
    
    #Display the paddle on the desired space
    def show_paddle(self,space):
        space.light_pixel(self.positionx,self.positiony+1,self.color)
        space.light_pixel(self.positionx,self.positiony,self.color)
        space.light_pixel(self.positionx,self.positiony-1,self.color)

    #Update height position of the paddle
    def move_paddle(self,y):
        self.positiony = y

    def erase_paddle(self,space):
        space.light_pixel(self.positionx,self.positiony+1,0)
        space.light_pixel(self.positionx,self.positiony,0)
        space.light_pixel(self.positionx,self.positiony-1,0)

#Translates xy pair to "yx" for reading by LaunchPad   
def pair_to_pixel(x,y):
    xstr = str(x)
    ystr = str(y)
    return int(ystr+xstr)

#Checks if the ball is near an edge
def check_ball(ball,space,paddle1,paddle2):
    if ball.positionx == (space.width-1):
        if paddle2.positiony == ball.positiony:
            ball.velocityx = -ball.velocityx
            ball.velocityy = 0
            print("Hit Right Paddle")
        elif paddle2.positiony == ball.positiony+1:
            ball.velocityx = -ball.velocityx
            ball.velocityy = -1
            print("Hit Right Paddle")
        elif paddle2.positiony == ball.positiony-1:
            ball.velocityx = -ball.velocityx
            ball.velocityy = 1
            print("Hit Right Paddle")
        else:
            winner.winner = 1
            player_wins(p1p,board)
            print("Player 1 Won")
    
    if ball.positionx == 2:
        if paddle1.positiony == ball.positiony:
            ball.velocityx = abs(ball.velocityx)
            ball.velocityy = 0
            print("Hit Left Paddle")
        elif paddle1.positiony == ball.positiony+1:
            ball.velocityx = abs(ball.velocityx)
            ball.velocityy = -1
            print("Hit Left Paddle")
        elif paddle1.positiony == ball.positiony-1:
            ball.velocityx = abs(ball.velocityx)
            ball.velocityy = 1
            print("Hit Left Paddle")
        else:
            winner.winner = 2
            player_wins(p2p,board)
            print("Player 2 Won")
    
    if ball.positiony >= space.height:
        print("Hit top bar")
        ball.velocityy = -ball.velocityy
    
    if ball.positiony <= 1:
        print("Hit bottom bar")
        ball.velocityy = abs(ball.velocityy)

def check_win(ball,space):
    if ball.positionx == (space.width):
        return True
    
    if ball.positionx == 1:
        return True

#Checks for input and moves paddle accordingly
def user_in(indata,package):

    noteread = dataIn[0][0][1]
    package = in_split(noteread,package)
    return(package)
        
#Splits an incoming string into [y,x]
def in_split(indata,package):
    newdata = str(indata)
    for letter in newdata:
        number = int(letter)
        package.append(number)
    return(package)

#Establish if incoming data is useable
def is_useable(indata):
    print(indata)
    noteread = "NODATA"
    try:
        noteread = dataIn[0][0][1]
        return True
    except:
        print("No MIDI Data!")
        noteread = "NODATA"
        return False
    finally:
        print(noteread)

#Player Wins
def player_wins(paddle,board):
    paddle.score = paddle.score + 1
    print("Made it to player wins")

#Check if someone won the whole game
def check_game(p1,p2):
    if p1.score > 9 or p2.score > 9:
        return True

#Print out a number on the display
def print_number(number,space,color):
    numberx = numbersx[number-1]
    numbery = numbersy[number-1]
    counter = 0
    while counter < len(numberx):
        space.light_pixel(numberx[counter],numbery[counter],color)
        counter = counter + 1

def ball_actions(paddle1,paddle2,ball,space):
    ball.erase_ball(board)
    check_ball(ball,space,paddle1,paddle2)
    winner.iswin = False
    winner.iswin = check_win(ball,space)
    ball.update_ball()
    ball.show_ball(space)

#BEGIN END OF DEFINITIONS
#Create the board and ballbag objects
board = Board(8,8)
bag = BallBag()

#Create the paddle objects
p1p = Paddle(1,5)
p2p = Paddle(8,45)

#Creates the ball object
bag.add_ball(Ball,4,4,32)
#bag.add_ball(Ball,4,4,3)

#Creates win state object
winner = Winner()

while True:
    #initialize player scores
    p1p.score = 0
    p2p.score = 0

    while True:
        #Clear the board
        board.clear_board()

        #Position the ball
        for ball in bag.balls:
            ball.positionx = random.randint(3,5)
            ball.positiony = random.randint(3,5)
            ball.velocityy = random.randint(-1,1)
            possibleballvx = [-1,1]
            ball.velocityx = possibleballvx[random.randint(0,1)]

        #Show game objects
        p1p.show_paddle(board)
        p2p.show_paddle(board)
        for ball in bag.balls:
            ball.show_ball(board)

        #Initialize score
        winner.winner = 0

        time.sleep(1)

        #Active round loop
        tickcounter = 0
        #Set speed between frames
        round_time = 0.1
        while True:

            '''
            for ball in bag.balls:
                ball.erase_ball(board)
                check_ball(ball,board)
                ball.update_ball()
                ball.show_ball(board)
            time.sleep(0.1)
            '''
            #BALL ACTIONS (Every 3 ticks)
            if tickcounter % 3 == 0:
                for balls in bag.balls:
                    ball_actions(p1p,p2p,balls,board)

            #Check if there's a win
            if winner.iswin == True:
                break

            #PADDLE ACTIONS
            #Erases current paddles
            p1p.erase_paddle(board)
            p2p.erase_paddle(board)

            #Read incoming MIDI data
            dataIn = midi_in.read(1)
            print(dataIn)

            #Check if the data coming in is useable
            dataUseable = True
            dataUseable = is_useable(dataIn)

            #Move paddle if the data is useable and relavent
            if dataUseable == True:
                userInputCoords = []
                userInputCoords = user_in(dataIn,userInputCoords)
                print(userInputCoords)
                if userInputCoords[1] == 1:
                    p1p.move_paddle(userInputCoords[0])
                elif userInputCoords[1] == 8:
                    p2p.move_paddle(userInputCoords[0])

                #Easter Egg
                if userInputCoords[1] == 2:
                    p1p.color = gameColors[p1p.colorIndex]
                    p1p.colorIndex = random.randint(0,(len(gameColors)-1))
                elif userInputCoords[1] == 7:
                    p2p.color = gameColors[p2p.colorIndex]
                    p2p.colorIndex = random.randint(0,(len(gameColors)-1))
            
            #Shows new paddles
            p1p.show_paddle(board)
            p2p.show_paddle(board)

            #Ending the round, increasing speed slightly
            time.sleep(round_time)
            round_time = round_time * 0.995

            tickcounter = tickcounter + 1

        #Shows the winner's score
        if winner.winner == 1:
            print("checked that 1 won")
            print_number(p1p.score,board,p1p.color)
        elif winner.winner == 2:
            print("checked that 2 won")
            print_number(p2p.score,board,p2p.color)
        time.sleep(2)

        #Ends the game if there is a winner
        wongame = False
        wongame = check_game(p1p,p2p)
        if wongame == True:
            break
    
    #flash winning player's colors until user input
    while True:

        #flash the board the winning player's colors
        if winner.winner == 1:
            board.fill_board(p1p.color)
        else:
            board.fill_board(p2p.color)
        time.sleep(1)
        board.fill_board(0)
        time.sleep(1)

        #Read incoming MIDI data
        dataIn = midi_in.read(1)
        print(dataIn)

        #Check if the data coming in is useable
        dataUseable = True
        dataUseable = is_useable(dataIn)

        #Break loop if data is useable
        if dataUseable == True:
            break
