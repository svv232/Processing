import copy
import xml.etree.ElementTree as etree

maxlat=40.6903
minlat=40.7061
maxlon=-73.9728
minlon=-74.0065

def mouseToScreen(mx,my):
    return (minlon+(mx/float(width))*(maxlon-minlon),
    minlat+(my/float(height))*(maxlat-minlat))

def getMap(file):
    """
    This loads the map and returns a pair (V,E)
    V contains the coordinates of the veritcies
    E contains pairs of coordinates of the verticies
    """
    G = open(file)
    root = etree.parse(G).getroot()
    v={}
    
    for child in root:
        if (child.tag=="node"):
            v[child.attrib["id"]]=(float(child.attrib["lon"]),float(child.attrib["lat"]))
    e=[]
    
    for child in root:
        if (child.tag=="way"):
            a=[]
            for gc in child:
                if gc.tag=="nd":
                    a.append(v[gc.attrib["ref"]])
            for i in range(len(a)-1):
                e.append((a[i],a[i+1]))
    return list(v.values()),e


class Graph:

  class _Vertex:
    def __init__(self,label=None):
      self._label = label
    
    def __hash__(self):
      return hash(id(self))
    
    def element(self):
      return self._label

  class _Edge:
    def __init__(self,origin,dest,name):
      self._origin,self._dest,self._name = origin,dest,name
    
    def endpoint(self):
      return (self._origin,self._dest)
    
    def opposite(self,v):
      return self._dest if self._origin == v else self._origin
    
    def element(self):
      return self._name
    
    def __hash__(self):
      return hash((self.endpoint()))
  

  def __init__(self):
    self._outgoing = {}

  
  def edges(self):
    edges = set()
    [edges.update(i.values()) for i in self._outgoing.values()]
    return edges


  def incident_edges(self,v):
    for i in self._outgoing[v].values():
        yield i

  def insert_vertex(self,label=None):
    retv = self._Vertex(label)
    self._outgoing[retv] = {}
    return retv

  def insert_edge(self,origin,dest,name=None):
    edge = self._Edge(origin,dest,name)
    self._outgoing[dest][origin] = edge
    self._outgoing[origin][dest] = edge



class Map:
    
    def __init__(self,V,E):
        self._G = Graph()
        self._colors = {}
        self._vertices = {}
        for i in V:
            self._vertices[i] = self._G.insert_vertex(i)
        for x,y in E:
            self._G.insert_edge(self._vertices[x],self._vertices[y])

    def BFS(self, s,distances=None):
        self._colors.clear()
        if distances is None:
            distances = {s:None}
        self._colors.clear()
        level = [s]
        r,g,b = 255,0,0
        while len(level) > 0:
            next_level = []
            for u in level:
                for e in self._G.incident_edges(u): 
                    v = e.opposite(u)
                    if v not in distances: 
                        distances[v] = e
                        next_level.append(v)
                        self._colors[e] = (r,g,b)
            r -= 4
            b += 4
            level = next_level
        
    def mapdraw(self):
        distance = {}
        clear()
        background(255)
        for i in self._G.edges():
            distance[i] = dist(mouseToScreen(mouseX,mouseY)[0],mouseToScreen(mouseX,mouseY)[1],i._dest.element()[0],i._dest.element()[1])
            if i not in self._colors:
                self._colors[i] = (105,105,105)
            stroke(*self._colors[i])
            line(i._origin.element()[0],i._origin.element()[1],i._dest.element()[0],i._dest.element()[1])
        m = min(distance.iteritems(),key=lambda x:x[1])[0]
        strokeWeight(0.0001)
        stroke(0,255,0)
        line(m._origin.element()[0],m._origin.element()[1],m._dest.element()[0],m._dest.element()[1])
        self.BFS(m._origin)



(V,E)=getMap("map.osm")

M = Map(V , E)


def setup():
    size(1200,800)

def draw(): 
    scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
    translate(-minlon,-minlat)
    strokeWeight(0.00001)
    M.mapdraw()