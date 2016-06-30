from Sphere import Sphere
from CameraMatrix import CameraMatrix
from ProjectionMatrix import ProjectionMatrix
from ActiveEdgeTable import ActiveEdgeTable
import numpy as np
import math

class Drawer:

    def __init__(self, raster):
        self.raster = raster
        self.sphere = None
        self.camMat = None
        self.projMat = None
        self.sorted = None
        self.point = None
        self.points = None
        self.triangles = None
        self.currTriangle = None
        self.texture = None
        self.pixels = None
        self.color = (174,198,207)

    def draw(self, photo, pixels):
        self.pixels = pixels
        self.texture = photo
        self.sphere = Sphere(500, 20, 20)
        self.camMat = CameraMatrix((700, 1, 1), (1, 1, 1))
        self.projMat = ProjectionMatrix(math.pi * (2.0 / 3.0), 800 / 600, 100, 1000)
        self.sphere.transform(self.camMat, self.projMat)
        self.triangles = self.sphere.getTriangles()
        for triangle in self.triangles:
            self.currTriangle = triangle
            self.getpoints(triangle)
            self.sorted = sorted(self.points, key=lambda tup: tup[1], reverse=True)
            self.fill()

    def getpoints(self, tr):
        x1 = int((tr.v1.p1[0])*400+400)
        y1 = int(-(tr.v1.p1[1])*300+300)
        x2 = int((tr.v2.p1[0]) * 400 + 400)
        y2 = int(-(tr.v2.p1[1]) * 300 + 300)
        x3 = int((tr.v3.p1[0]) * 400 + 400)
        y3 = int(-(tr.v3.p1[1]) * 300 + 300)
        self.points=((x1,y1), (x2,y2), (x3,y3))


    def interpolate(self, p):
        p1 = (p[0]/float(400)-1, 1-(p[1]/float(300)))
        xVertex = self.currTriangle.getBestScaleVertex(0)
        yVertex = self.currTriangle.getBestScaleVertex(1)
        xscale =float(xVertex.t[0])/float(xVertex.p1[0])
        yscale =float(yVertex.t[1])/float(yVertex.p1[1])
        x = p1[0] * xscale
        y = p1[1] * yscale
        imgX = x*(self.texture.size[0])
        if(imgX == self.texture.size[0]):
            imgX -= 1
        imgY = (y*self.texture.size[1])
        if (imgY == self.texture.size[1]):
            imgY -= 1
        return int(imgX), int(imgY)


    def putpixel(self, x, y, val):
        p = self.interpolate((x, y))
        try:
            r,g,b = self.pixels[p[0], p[1]]
        except IndexError:
            r = 127
            g = 127
            b = 127
        self.raster.put('#%02x%02x%02x' % (r,g,b), (x, y))

    def fill(self):
        n = len(self.points)
        k = 0
        ymax = self.sorted[0][1]
        ymin = self.sorted[len(self.sorted) - 1][1]
        aet = ActiveEdgeTable()
        for y in range(ymax, ymin + 1, -1):
            while k <= n and self.sorted[k][1] == y:
                i = self.points.index(self.sorted[k])
                if self.points[(i - 1) % n][1] < self.points[i][1]:
                    aet.add(self.points[i][0], self.points[i][1], self.points[(i - 1) % n][0],
                            self.points[(i - 1) % n][1])
                elif self.points[(i - 1) % n][1] > self.points[i][1]:
                    aet.removeEdge(self.points[(i - 1) % n][0], self.points[(i - 1) % n][1], self.points[i][0],
                                   self.points[i][1])
                if self.points[(i + 1) % n][1] < self.points[i][1]:
                    aet.add(self.points[i][0], self.points[i][1], self.points[(i + 1) % n][0],
                            self.points[(i + 1) % n][1])
                elif self.points[(i + 1) % n][1] > self.points[i][1]:
                    aet.removeEdge(self.points[(i + 1) % n][0], self.points[(i + 1) % n][1], self.points[i][0],
                                   self.points[i][1])
                k = k + 1
            j = 0
            aet.sort()
            while (j <= len(aet.edges) - 2):
                for xx in range(int(math.ceil(aet.edges[j].x)), int(round(aet.edges[j + 1].x))):
                    self.putpixel(xx, y, self.color)
                j = j + 2
            aet.remove(y)
            aet.update()

