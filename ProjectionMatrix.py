import numpy as np
import math


class ProjectionMatrix:

    @staticmethod
    def ctg(a):
        return 1/math.tan(a)

    def __init__(self, fov, a, n, f):
        r1 = np.array([self.ctg(fov/2), 0, 0, 0])
        r2 = np.array([0, self.ctg(fov/2)/a, 0, 0])
        r3 = np.array([0, 0, -f/(f-n), (-f*n)/(f-n)])
        r4 = np.array([0, 0, -1, 0])
        self.matrix = np.vstack((r1, r2, r3, r4))