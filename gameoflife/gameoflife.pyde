board = [[0 for i in range(58)] for x in range(58)]
neighbors = [[0 for i in range(58)] for x in range(58)]
pause = False
reset = False
class Grid:
    global board
    def __init__(self, spaces):
        self.spaces = spaces
    def griddraw(self):
        x,y = (0,0)
        for row in range(len(board)):
            for column in range(len(board)):
                rect(x,y,w,w)
                x += w
            y += w
            x = 0
    def randomstart(self):
        import random
        y = (False,)
        for row in range(1, len(board) - 1):
            for column in range(1, len(board)-1):
                x = random.randint(0, len(y) - 1)
                board[row][column] = y[x]


class Rules(Grid):
    global board
    def __init__(self, spaces, board):
        Grid.__init__(self, spaces)
        self.board = [[False for x in range(self.spaces)] for x in range(self.spaces)]
        self.neighbors =[[False for x in range(self.spaces)] for x in range(self.spaces)]
    def rules(self):
        for row in range(1, len(board) - 1):
            for column in range(1, len(board) - 1):
                count = 0
                if board[row - 1][column - 1]:
                    count += 1
                if board[row - 1][column]:
                    count += 1
                if board[row - 1][column + 1]:
                    count += 1
                if board[row][column - 1]:
                    count += 1
                if board[row][column + 1]:
                    count += 1
                if board[row + 1][column - 1]:
                    count += 1
                if board[row + 1][column]:
                    count += 1
                if board[row + 1][column + 1]:
                    count += 1
                if count < 2 and board[row][column]:
                    self.board[row][column] = False
                    self.neighbors[row][column] = count
                elif count > 3 and board[row][column]:
                    self.board[row][column] = False
                    self.neighbors[row][column] = count
                elif (count == 2 or count == 3) and board[row][column]:
                    self.board[row][column] = True
                    self.neighbors[row][column] = count
                elif board[row][column] == False and count == 3:
                    self.board[row][column] = True
                    self.neighbors[row][column] = count
                else:
                    self.board[row][column] = False
                    self.neighbors[row][column] = count
        return self.board
    def neighbor(self):
        return self.neighbors
    
    
class Colors(Rules):
    global board
    global neighbors
    def __init__(self, spaces):
        Rules.__init__(self, spaces, board)
        self.colors = ((139,0,0),(0,191,255),(0,0,0),(25,25,112),(255,255,255),(255,20,147))
        #self.colors = ("Red", "Cyan", "Green", "Purple", "White") 

    def colordraw(self, board):
        x,y = (0,0)
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == True:
                    if neighbors[row][column] < 2:
                        fill(*self.colors[5])
                    elif neighbors[row][column] > 3:
                        fill(*self.colors[2])
                    elif neighbors[row][column] == 2:
                        fill(*self.colors[1])
                    elif neighbors[row][column] == 3:
                        fill(*self.colors[0])
                elif board[row][column] == False:
                        fill(*self.colors[4])
                rect(x,y,w,w)            
                x += w
            y += w
            x = 0
                    
def setup():
    c = Colors(15)
    size(878, 878)
    g.griddraw()
    g.randomstart()
    c.colordraw(board)

w = 200/13 #width of boxes
g = Grid(15) #object from the grid class

def keyPressed():
    global pause
    global reset
    if key == " ":
        pause = not pause
    if key == "s":
        reset = True

def mousePressed():
    global clicked
    global board
    c = Colors(15)
    board[mouseY//w][mouseX//w] = not board[mouseX//w][mouseY//w]
    c.colordraw(board)
    
    
def draw():
    global board
    global neighbors
    global pause
    global reset
    frameRate(20)
    c = Colors(15)
    r = Rules(58, board)
    if pause == False:
        board = r.rules()
        c.colordraw(board)
        neighbors = r.neighbor()
        clicked = False
    if reset == True:
        g.griddraw()
        g.randomstart()
        c.colordraw(board)
        reset = False