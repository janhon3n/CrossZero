from player import *
from stage import *
from window import *
from event import *

DRAW = True


#function to play a game
def playGame(stage, player1, player2, stageChangedEvent):
    turn = 1
    while not stage.isFull() and not stage.getWinner():
        if turn == 1:
            move = player1.getMove()
            while(stage.place(player1.type, move[0], move[1]) == -1):
                move = player1.getMove()
            stageChangedEvent.__call__(player1.type, move[0], move[1])
            turn = 0
        else:
            move = player2.getMove()
            while(stage.place(player2.type, move[0], move[1]) == -1):
                move = player2.getMove()
            stageChangedEvent.__call__(player2.type, move[0], move[1])
            turn = 1



# 0 = tyhjä, 1= risti, 2= nolla

rows = 3
cols = 3

stage = Stage(rows, cols)

if(DRAW):
    width = 300
    height = 300
    win = GameWindow("CrossZero", width, height)
    win.initWindow(stage)

p1 = RandomPlayer(rows, cols, 1)
p2 = HumanPlayer(rows, cols, 2, win)

def stageChanged(type, row, col):
    if(DRAW):
        win.drawNewItem(type, row, col)
    print(stage.stage)

e = Event([stageChanged])
playGame(stage, p1, p2, e)
try:
    win.getMouse()
except Exception:
    print("Closing")