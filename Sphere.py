from Vertex import Vertex
from Triangle import Triangle
import math


class Sphere:

    def __init__(self, rad, m, n):
        self.r = float(rad)
        self.m = m
        self.n = n
        self.vertices = []
        p = (0, self.r, 0, 1)
        v = (0, 1, 0, 0)
        t = (1, 0.5)
        self.vertices.append(Vertex(p, v, t))
        i=1
        while i<=n :
            j = 1
            while j<=m:
                x = self.r * math.cos(((2*math.pi)/float(self.m))*(j-1)) * math.   sin((math.pi/(float(self.n) + 1))*i)
                y = self.r * math.cos((math.pi/(float(self.n)+1))*i)
                z = self.r * math.sin(((2*math.pi)/float(self.m))*(j-1))*math.sin((math.pi/(float(self.n+1)))*i)
                p = (x, y, z, 1)
                v = (x/self.r, y/self.r, z/self.r, 0)
                t = ((j-1)/(float(m)-1), i/(float(n) + 1))
                self.vertices.append(Vertex(p,v,t))
                j=j+1
            i=i+1
        p = (0, -self.r, 0, 1)
        v = (0, -1, 0, 0)
        t = (0, 0.5)
        self.vertices.append(Vertex(p,v,t))

    def transform(self, camMat, projMat):
        for vertex in self.vertices:
            vertex.transform(camMat, projMat)

    def getTriangles(self):
        ret =[]
        i = 0
        while i <= self.m - 2:
            triangle = Triangle(self.vertices[0], self.vertices[i+2], self.vertices[i+1])
            if triangle.check():
                ret.append(triangle)
            i = i + 1
        tr = Triangle(self.vertices[0], self.vertices[1], self.vertices[self.m])
        if tr.check():
            ret.append(tr)
        i = 0
        while i <= self.m - 2:
            triangle = Triangle(self.vertices[self.m * self.n], self.vertices[(self.n - 1)*self.m +i+1], self.vertices[(self.n - 1)*self.m +i+2])
            if triangle.check():
                ret.append(triangle)
            i = i + 1
        tr = Triangle(self.vertices[self.m*self.n+1], self.vertices[self.m*self.n], self.vertices[(self.n-1)*self.m+1])
        if tr.check():
            ret.append(tr)
        i = 0
        while i <= self.n - 2:
            j=1
            while j <= self.m - 1:
                triangle = Triangle(self.vertices[i*self.m+j], self.vertices[i*self.m+j+1], self.vertices[(i+1)*self.m+j+1])
                if triangle.check():
                    ret.append(triangle)
                triangle = Triangle(self.vertices[i*self.m+j], self.vertices[(i+1)*self.m+j+1], self.vertices[(i+1)*self.m+j])
                if triangle.check():
                    ret.append(triangle)
                j=j+1
            tr = Triangle(self.vertices[(i+1)*self.m], self.vertices[i*self.m+1], self.vertices[(i+1)*self.m+1])
            if tr.check():
                ret.append(tr)
            tr = Triangle(self.vertices[(i+1)*self.m],self.vertices[(i+1)*self.m+1], self.vertices[(i+2)*self.m])
            if tr.check():
                ret.append(tr)
            i += 1
        return ret





