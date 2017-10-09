class Board:
  class _item:
    def __init__(self,f):
      self._p = set(range(1,10))
      self._f = f

  
  def __init__(self,A):
    self._grid = {}
    self._board = [list(map(self._item,i)) for i in A]
    for box in range(len(A)):
      for row in range(9):
        self._grid[self._board[box][row]] = (box,row)

  def _remove(self,i,uset):
    if isinstance(i._f,str):
      i._p.difference_update(uset)
      if len(i._p) == 1:
        i._f = i._p.pop()
        self.x_solve(i)

  def Bprint(self):
    for i in self._board:
      print([x._f for x in i])

  def board(self):
    return [[i._f for i in x] for x in self._board]

  def Sprint(self):
    for i in self._board:
      for j in i: 
        print(j._p)
  
  def x_solve(self,i):
    self.row_update(self._grid[i][0])
    self.column_update(self._grid[i][1])

  def _square_collect(self,cols=0,rows=0):
    uset = {self._board[rows+i][cols+j]._f for i in range(3) for j in range(3) if
    isinstance(self._board[rows+i][cols+j]._f,int)}
    return uset

  def _row_collect(self,rows=0):
    return {i._f for i in self._board[rows] if i._f != " "}

  def _column_collect(self,cols=0):
    return {self._board[i][cols]._f for i in range(9) if self._board[i][cols]._f != " "}

  def square_update(self,cols=0,rows=0):
    uset = self._square_collect(cols,rows)
    [self._remove(self._board[rows+i][cols+j],uset) for i in range(3) for j in range(3)]

  def row_update(self,rows=0):
    uset = self._row_collect(rows)
    [self._remove(i,uset) for i in self._board[rows]]

  def column_update(self,cols=0):
    uset = self._column_collect(cols)
    [self._remove(self._board[i][cols],uset) for i in range(9)]

def solve(B):
  for i in range(0,7,3): 
    for j in range(0,7,3):
      B.square_update(i,j)
  for i in range(9):
    B.row_update(i)
    B.column_update(i)

A = [[5,' ',' ',' ',' ',4,' ',' ',6],
  [' ',' ',' ',5,7,' ',' ',' ',' '],
  [2,' ',7,' ',' ',' ',' ',' ',' '],
  [' ',9,5,' ',2,1,' ',' ',3],
  [' ',' ',6,3,' ',8,' ',5,9],
  [' ',7,' ',' ',' ',' ',' ',' ',4],
  [6,' ',' ',' ',3,' ',8,' ',' '],
  [8,' ',' ',4,1,' ',' ',' ',5],
  [' ',5,4,8,6,' ',' ',' ',' ',]]



b = Board(A)

def setup():
    size(500,500)
    draw_board(A)

def draw(): pass    

def keyPressed():
    if key == " ":
        solve(b)
        draw_board(b.board())
    if key == 'r':
        setup()
        
def draw_board(A):
    d = (500 / 9)
    x,y = 0,d
    for i in range(9):
        for j in range(9):
            fill(255)
            rect(x,y-d,d,d)
            fill(0)
            textSize(32)
            textAlign(LEFT)
            text(A[i][j],x+15,y-10)
            x += d
        x = 0
        y += d 

  