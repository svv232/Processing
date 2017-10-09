num = 50
x =[None for i in range(num)]
y =[None for i in range(num)]
vx = [0 for i in range(num)]
vy = [0 for i in range(num)]
ax = [0 for i in range(num)]
ay = [0 for i in range(num)]
 
height = 800
width = 800


magnetism = 10.0
radius = 1
shinyshit = .95

def setup():
    size(height,width)
    noStroke()
    fill(0)
    ellipseMode(RADIUS)
    background(0)
    blendMode(ADD)

for i in range(num):
    x[i] = random(width)
    y[i] = random(height)


def draw():
    fill(0,0,0)
    rect(0,0,width,height)    
    
    for i in range(num):
        distance = dist(mouseX, mouseY, x[i], y[i])
        if distance > 3:
            ax[i] = magnetism * (mouseX-x[i]) / (distance**2)
            ay[i] = magnetism * (mouseY-y[i]) / (distance**2)
        vx[i] += ax[i]
        vy[i] += ay[i]
        
        vx[i] = vx[i]*shinyshit
        vy[i] = vy[i]*shinyshit
        
        x[i] += vx[i]
        y[i] += vy[i]
        
        other = dist(0,0,vx[i],vy[i])
        r = map(other, 0,0,0,155)
        g = map(other, 0,64,0,155)
        b = map(other, 0,128,0,155)
        fill(r,g,b,32);
        ellipse(x[i],y[i],radius,radius)