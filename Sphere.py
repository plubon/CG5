from Vertex import Vertex
import math

class Sphere:

    def __init__(self, rad, m, n):
        self.r = rad
        self.m = m
        self.n = n
        self.vertices = []
        for idx in xrange(m*n+2):
            if idx == 0:
                p = (0, self.r, 0, 1)
                v = (0, 1, 0, 0)
                t = (1, 0.5)
                self.vertices.append(Vertex(p, v, t))
            elif idx < self.m * self.n + 1:
                i = idx//m;
                j = idx % m;
                x = self.r * math.cos(((2*math.pi)/self.m)*(j-1)) * math.   sin((math.pi/(self.n + 1))*i)
                y = self.r * math.cos((math.pi/(self.n+1))*i)
                z = self.r * math.sin(((2*math.pi)/self.m)*(j-1))*math.sin((math.pi/(self.n+1))*i)
                p = (x, y, z, 1)
                v = (x/self.r, y/self.r, z/self.r, 0)
                t = ((j-1)/(m-1), i/(n + 1))
                self.vertices.append(Vertex(p,v,t))
            elif idx == self.m * self.n + 1:
                p = (0, -self.r, 0, 1)
                v = (0, -1, 0, 0)
                t = (0, 0.5)
                self.vertices.append(Vertex(p,v,t))
        print len(self.vertices)



