from Sphere import Sphere
from CameraMatrix import CameraMatrix
from ProjectionMatrix import ProjectionMatrix
from ActiveEdgeTable import ActiveEdgeTable
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
        self.color = (174,198,207)

    def draw(self):
        self.sphere = Sphere(300, 10, 10)
        self.camMat = CameraMatrix((700, 1, 1), (1, 1, 1))
        self.projMat = ProjectionMatrix(math.pi * (2.0 / 3.0), 1024 / 768, 100, 1000)
        self.sphere.transform(self.camMat, self.projMat)
        self.triangles = self.sphere.getTriangles()
        for triangle in self.triangles:
            self.getpoints(triangle)
            self.sorted = sorted(self.points, key=lambda tup: tup[1], reverse=True)
            self.fill()

    def getpoints(self, tr):
        x1 = int((tr.v1.p1[0])*512+512)
        y1 = int(-(tr.v1.p1[1])*384+384)
        x2 = int((tr.v2.p1[0]) * 512 + 512)
        y2 = int(-(tr.v2.p1[1]) * 384 + 384)
        x3 = int((tr.v3.p1[0]) * 512 + 512)
        y3 = int(-(tr.v3.p1[1]) * 384 + 384)
        self.points=((x1,y1), (x2,y2), (x3,y3))


    def putpixel(self, x, y, val):
        self.raster.put('#%02x%02x%02x' % val, (x, y))

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

