
sunLocation=(250,250)
sunRadius=50
yellow=(255,255,0)

earthRadius=30
blue=(0,0,255)
earthOrbitalRadius=170
earthSpeed=0.5

marsRadius=20
red=(255,0,0)
marsOrbitalRadius=80
marsSpeed=1

moonRadius=10
white=(255,255,255)
moonOrbitalRadius=45
moonSpeed=2.3

def getLocation(orbitAroundLocation,orbitRadius,speed,time):
    centerX=orbitAroundLocation[0]+orbitRadius*sin(speed*time)
    centerY=orbitAroundLocation[1]+orbitRadius*cos(speed*time)
    return (centerX,centerY)


def setup():
    size(500,500)
    global t
    global Planets
    t=0

def draw():
    global sun
    global t
    t+=0.02
    background(0)
    for p in Planets:
        p.draw(t)

def drawCelestialBody(location,radius,color):
    fill(*color)
    locX,locY=location
    ellipse(locX,locY,radius*2,radius*2)    


class Sun:
    def __init__(self, Sunlocation, sunRadius,color):
        self.Sunlocation = (250, 250)
        self.radius = 50
        self.color = (255,255,0)
        self.ls = []
    def draw(self, t):
        drawCelestialBody(self._getLocation(t),self.radius, self.color)
        for i in self.ls:
            i.draw(t)
    def _getLocation(self,t):
        return self.Sunlocation
    def addPlanet(radius,OrbitalRadius,color,Speed):
        x = (Planet(self, radius,OrbitalRadius,color,Speed))
        self.ls.append(x)
        return x
        

class Planet(Sun):
    def __init__(self, orbit, radius, orbitradius, color, speed):
        self.radius = radius
        self.orbitradius = orbitradius
        self.color = color
        self.speed = speed
        self.orbit = orbit
        self.ls = []
    def _getLocation(self,t):
            return getLocation(self.orbit._getLocation(t), self.orbitradius, self.speed, t)


sun=Sun(sunLocation,sunRadius,yellow)
earth=Planet(sun,earthRadius,earthOrbitalRadius,blue,earthSpeed)
mars=Planet(sun,marsRadius,marsOrbitalRadius,red,marsSpeed)
moon=Planet(earth,moonRadius,marsOrbitalRadius,white,moonSpeed)
Planets=[sun,earth,mars,moon]