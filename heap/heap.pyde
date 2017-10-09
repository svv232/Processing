#Just Call draw_tree on the root node and it will draw the tree
#Your node class must use ._l ._r and ._data
def subtree_size(node):
    if node is None:
      return 0
    else:
      return 1+subtree_size(node._left)+subtree_size(node._right)

def draw_tree(node,level=1,x=20,parx=None,pary=None):
    XSEP=15
    YSEP=30
    fill(0)
    textAlign(CENTER,CENTER)
    textSize(15)
    lsize=subtree_size(node._left)
    myx,myy=x+lsize*XSEP,YSEP*level
    text(str(node._data),myx,myy)
    if node._left is not None:
      draw_tree(node._left,level+1,x,myx,myy)
    if node._right is not None:
      draw_tree(node._right,level+1,x+(lsize+1)*XSEP,myx,myy)
    if parx is not None:
      strokeWeight(10)
      stroke(0,255,0,30)
      line(parx,pary,myx,myy)
#--------------------------------------------
class PQ:
    class _Node:
        def __init__(self,left,right,data):
            self._left = left
            self._right = right
            self._data = data
    
    def __init__(self,n=None): self._root = n
    
    def flip(self,node): node._left,node._right = node._right,node._left
    
    def _merge_left(self,node1,node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        if node1._data < node2._data:
            node1._left = self._merge_left(node2,node1._left)
            self.flip(node1)
            return node1
        else:
            node2._left = self._merge_left(node1,node2._left)
            self.flip(node2)
            return node2
    
    def merge(self,heap): self._root = self._merge_left(self._root,heap._root)
    
    def insert(self,v): self.merge(PQ(self._Node(None,None,v)))
    
    def extractMin(self):
        minimum = self._root._data
        self._root = self._merge_left(self._root._left,self._root._right)
        return minimum
#-------------------------------------------------------
import random
A=list(range(20))
random.shuffle(A)
pq=PQ()
for i in A:
    pq.insert(i)
print([pq.extractMin() for i in range(20)])

for i in range(20):
    pq.insert(i)

def setup():
    size(1000,1000)

def draw():
    draw_tree(pq._root)