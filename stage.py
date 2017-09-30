
#Stage class
class Stage:
    rows = 0
    cols = 0
    goal = 0

    stage = []

    def __init__(self, rows=3, cols=3, goal=3):
        self.rows = rows
        self.cols = cols
        self.goal = goal
        self.stage = [[0 for x in range(cols)] for y in range(rows)]

    def place(self, type, row, col):
        if(self.stage[row][col] == 0):
            self.stage[row][col] = type
            return 0
        return -1

    def getWinner(self):
        return 0

    def isFull(self):
        isfull = True
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.stage[i][j] == 0):
                    isfull = False
        return isfull

