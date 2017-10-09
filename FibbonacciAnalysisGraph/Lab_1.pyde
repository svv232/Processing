from __future__ import print_function

def fib1(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib1(x-1)+fib1(x-2)
def fib2(x):
    A=[]
    A.append(0)
    A.append(1)
    for i in range(2,x+1):
        A.append(A[i-1]+A[i-2])
    return A[x]

def fib3(x):
    if x==0:
        return 0
    else:
        a=0
        b=1
    for i in range(x-1):
        a,b=b,a+b
    return(b)

def fib3(x):
    if x==0:
        return 0
    else:
        a=0
        b=1
    for i in range(x-1):
        a,b=b,a+b
    return(b)
"""
for f in (fib1,fib2,fib3):
    print([f(i) for i in range(10)])
"""

import timeit
def timeFunction(f,n,repeat=1):
    return timeit.timeit(f.__name__+'('+str(n)+')', 
        setup="from __main__ import "+f.__name__,number=repeat)/repeat

'''
def printFunctionTimes(x, y):
    for i in y:
        print("n ="+ str(i)+":",x[0].__name__, + timeFunction(fib1,i),x[1].__name__, + timeFunction(fib1,i),x[2].__name__, + timeFunction(fib1,i))
'''

def setup():
    size(500, 500) #sets the size of the window
    global fp
    fp=fp=functionsPlotter( (runprefix_average1,runprefix_average2,runprefix_average3),((255,0,0),(0,255,0),(0,0,255)),10)

    
def draw():
    global fp
    background(255) #Background is black
    fp.timeNext()
    fp.plot()
    
"""
class functionPlotter:
    def __init__(self, f,inc=1):
        self.f = f
        self.t = []
        self.n = 1
        self.inc = inc
    def timeNext(self):
        self.t.append(timeFunction(self.f, self.n))
        self.n += self.inc
    def plot(self):
        scale_x = float(width) / len(self.t)
        scale_y = height / max(.00001, max(self.t))
        for i in range(len(self.t) - 1):
            line(i * scale_x, height - (self.t[i] * scale_y), (i + 1) * scale_x, height -  (self.t[i + 1] * scale_y))
"""        
            
class functionsPlotter:
    def __init__(self, functions, colors, inc=1):
        self._functions = functions
        self._times = [[] for f in functions]
        self._n = 1
        self._inc = inc
        self._colors = colors

    def timeNext(self):
        for i in range(len(self._functions)):
            self._times[i].append(timeFunction(self._functions[i], self._n))
        self._n += self._inc

    def plot(self):
        scaley = height / \
            max(0.00001, max([max(times) for times in self._times]))
        scalex = float(width) / len(self._times[0])
        for fi in range(len(self._functions)):
            stroke(*self._colors[fi])
            for i in range(len(self._times[fi]) - 1):
                line(i *scalex, height - self._times[fi][i ] * scaley, 
                    (i+1)*scalex, height - self._times[fi][i+1]* scaley)
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n # create new list of n zeros
    for j in range(n):
        total = 0 # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
        total += S[i]
        A[j] = total / (j + 1) # record the average
    return A

def runprefix_average1(n):
    prefix_average1(range(n))

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1) # record the average
    return A

def runprefix_average2(n):
    prefix_average2(range(n))

def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n # create new list of n zeros
    total = 0 # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j] # update prefix sum to include S[j]
        A[j] = total / (j + 1) # compute average based on current sum
    return A

def runprefix_average3(n):
    prefix_average3(range(n))