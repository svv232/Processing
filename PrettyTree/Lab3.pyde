import sys
import random
import math
def setup():
  size(1100, 800)
  background(255)
  pixelDensity(displayDensity())
  
def drawLineAngle(color, start, angle, length, width=1):
  angle += 180 # make up zero degrees
  end = (start[0] + math.sin(math.radians(angle)) * length,
  start[1] + math.cos(math.radians(angle)) * length)
  stroke(*color)
  if width:
    strokeWeight(width)
  else:
    noStroke()
  line(*(start + end))
  return end

def drawLeaf(location):
  y = ((255,255,255),(199,21,133))
  stroke(0, 50, 0)
  fill(*y[random.randint(0,1)])
  strokeWeight(0.5)
  ellipse(location[0],location[1],3.5,3.5)


def drawTree(start,leaf,leaves,c=0,angle=0,branch_w=25,branch_l=170,angle_offset=40):
  end = drawLineAngle((63,37,11),start,angle,branch_l,branch_w)
  endL = drawLineAngle((63,37,11),end,angle+angle_offset+10*math.atan2(mouseY,-mouseX/100),branch_l*.67,branch_w*.8)
  endR = drawLineAngle((63,37,11),end,angle-angle_offset+1/10*math.atan2(mouseY,-mouseX/100),branch_l*.67,branch_w*.8)
  if leaf:
    drawLeaf(endL)
    drawLeaf(endR)
  if leaves < c:
      return
  else:
      drawTree(end,leaf,leaves,c+1,angle+angle_offset,branch_w*.8-.25,3+ branch_l*.67,angle_offset-2),drawTree(end,leaf,leaves,c+1,angle-angle_offset,branch_w*.8-.25,7+ branch_l*.67,angle_offset-2)


def keyPressed():
  global leaf
  if key=="l":
    leaf = not leaf    
    
def setup():
  global leaf
  leaf=True
  
def draw():
  clear()
  background(255)
  drawTree((550,800),leaf,12)
  noLoop()
  
  