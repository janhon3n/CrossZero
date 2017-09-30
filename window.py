from graphics import *

class GameWindow(GraphWin):
    #Graphics
    rows = 0
    cols = 0
    counter = 1

    def __init__(self, title, width, height):
        super(GameWindow, self).__init__(title, width, height)

    def initWindow(self, stage):
        self.rows = stage.rows
        self.cols = stage.cols

        for i in range(self.rows-1):
            l = Line(Point((self.width / stage.rows)*(i+1), 0), Point((self.width/stage.rows)*(i+1), self.height))
            l.draw(self)

        for i in range(self.cols-1):
            l = Line(Point(0, (self.height / stage.cols)*(i+1)), Point(self.width, (self.height / stage.cols) * (i+1)))
            l.draw(self)

    def drawNewItem(self, item, row, col):
        boxw = self.width / self.rows
        boxh = self.height / self.cols
        x = row*boxw + (boxw / 2)
        y = col*boxh + (boxh / 2)
        padding = 30
        if(item == 1):
            c = Circle(Point(x,y),boxw/2 - padding)
            c.setWidth(3)
            c.draw(self)
        elif(item == 2):
            l1 = Line(Point(x-(boxw/2)+padding, y-(boxh/2)+padding), Point(x+(boxw/2)-padding, y+(boxh/2)-padding))
            l2 = Line(Point(x-(boxw/2)+padding, y+(boxh/2)-padding), Point(x+(boxw/2)-padding, y-(boxh/2)+padding))
            l1.setWidth(3)
            l2.setWidth(3)
            l1.draw(self)
            l2.draw(self)

        tpadding = 10
        t = Text(Point(x-(boxw/2)+tpadding,y-(boxh/2)+tpadding), str(self.counter))
        t.draw(self)
        self.counter += 1