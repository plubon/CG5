import numpy as np


class Vertex:

    def __init__(self, p, v, t):
        self.point = p
        self.v = v
        self.t = t
        self.p1 = None
        self.p2 = None

    def transform(self, camMat, projMat):
        cam = np.dot(camMat.matrix, np.array(self.point))
        self.p2 = np.dot(projMat.matrix, cam)
        self.p1 = np.divide(self.p2, self.p2[3])


