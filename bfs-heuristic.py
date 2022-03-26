## Schema, ie classes templates
statevector = []

import math

def search(mat, x):
    for i in range(len(mat)):
        row = mat[i]
        for j in range(len(row)):
            e = mat[i][j]
            if(e==x):
                return (i, j)
    return (-1, -1)

class Board:
    def __init__(self, board=[]):
        self.board = board
        self.NOT_VALID = False
        self.checkEmpty()
        
    def change(self, i, j, v):
        self.board[i, j] = v
        
    def checkEmpty(self):
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(len(row)):
                if(self.board[i][j] == -1):
                    self.eX = i
                    self.eY = j
                    return
                
    def verifyValid(self):
        self.checkEmpty()
        if(self.NOT_VALID): return False
        
        if(self.eX < 0 or self.eX > len(self.board)-1 or self.eY < 0 or self.eY > len(self.board)-1): return False
        return True
    
    @staticmethod
    def hx(c, t): # Heuristic value
        h = 0
        for i in range(len(c.board)):
            row = c.board[i]
            for j in range(len(row)):
                e1 = c.board[i][j]
                (ti, ty) = search(t.board, e1)
                h = h + 1
        return h


    def swap(self, ix, iy, tx, ty):
        try:
            self.board[ix][iy], self.board[tx][ty] = self.board[tx][ty], self.board[ix][iy]
        except Exception as e:
            self.NOT_VALID = True
    
    def copy(self):
        b = Board()
        b.board = [x[:] for x in self.board]
        b.eX = self.eX
        b.eY = self.eY
        return b
    
    def __eq__(self, t):
        return self.board == t.board
    
    def __repr__(self):
        s = "A simple board with state\n"
        for row in self.board:
            s += str(' '.join([str(i) for i in row]))
            s+="\n"
        s+="Empty spot at pos %d, %d"%(self.eX, self.eY)
        return s

class TNode:
    def __init__(self, init, childs=[]):
        self.parent = None
        self.h = None
        self.state = init
        self.childs = childs
            
    def walkAndH(self, fin):
        # Assume hole in center
        board = self.state
        self.childs = []
        
        c = board.copy()
        c.swap(c.eX, c.eY, c.eX + 1, c.eY) ## Swap right
        if(c.verifyValid()):
            self.childAppend(c, fin)
            
        c = board.copy()
        c.swap(c.eX, c.eY, c.eX - 1, c.eY) ## Swap left
        if(c.verifyValid()):
            self.childAppend(c, fin)
            
        c = board.copy()
        c.swap(c.eX, c.eY, c.eX, c.eY + 1) ## Swap Up
        if(c.verifyValid()):
            self.childAppend(c, fin)
            
        c = board.copy()
        c.swap(c.eX, c.eY, c.eX, c.eY - 1) ## Swap Down
        if(c.verifyValid()):
            self.childAppend(c, fin)

            
    def childAppend(self, obj, fin):
        global statevector
        if(obj is not self.parent and obj not in statevector):
            statevector.append(obj) # Append into global state list ie CLOSED LIST
            
            t = TNode(obj)
            t.parent = self
            t.h = Board.hx(obj, fin)
            self.childs.append(t)
            
    def __repr__(self):
        s = "TNode with data: %s && Childs: %d"%(self.state, len(self.childs))
        return s
    
    def copy(self):
        t = TNode(self.state)
        return t

    def __eq__(self, other):
        return self.h == other.h

    def __lt__(self, other):
        return self.h < other.h
    

initialData = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10,11, 12],[13, 14, 15, -1]]
initBoard = Board(initialData)

finalData = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10,11, -1],[13, 14, 15, 12]]
finBoard = Board(finalData)

parent = TNode(initBoard)
q = [ parent ]
FOUND = False
fNode = None
while(q):
    e = q.pop(0)
    if(e.state == finBoard):
        FOUND = True
        fNode = e
        break
    e.walkAndH(finBoard)
    c = e.childs
    q.extend(c)

    q = sorted(q) # Sort and choose best elements

def rPrint(x):
    if(x is None): return
    rPrint(x.parent)
    print(x.state)

if(FOUND):
    print("found at")
    print(fNode)
    print("Tracing path")
    x = fNode
    rPrint(x)