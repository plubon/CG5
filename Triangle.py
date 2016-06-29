import numpy as np


class Triangle:

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def check(self):
        a1 = np.array([self.v2.p1[0] - self.v1.p1[0], self.v2.p1[1] - self.v1.p1[1], 0])
        a2 = np.array([self.v3.p1[0] - self.v1.p1[0], self.v3.p1[1] - self.v1.p1[1], 0])
        result = np.cross(a1, a2)
        if result[2] > 0:
            return True
        else:
            return False
