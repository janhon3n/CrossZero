from random import randint
import math

#Player classes
class Player:
    type = 0
    rowCount = 0
    colCount = 0

    def __init__(self, rowCount=3, colCount=3, type=0):
        self.rowCount = rowCount
        self.colCount = colCount
        self.type = type

    def getMove(self):
        return -1



class RandomPlayer(Player):
    def __init__(self, rowCount, colCount, type):
        super(RandomPlayer, self).__init__(rowCount, colCount, type)

    def getMove(self):
        return [randint(0,self.rowCount-1), randint(0,self.colCount-1)]



class HumanPlayer(Player):
    def __init__(self, rowCount, colCount, type, window):
        super(HumanPlayer, self).__init__(rowCount, colCount, type)
        self.window = window

    def getMove(self):
        point = self.window.getMouse()
        xper = point.x / self.window.width
        yper = point.y / self.window.height
        row = math.floor(xper * self.rowCount)
        col = math.floor(yper * self.colCount)
        return [row, col]
