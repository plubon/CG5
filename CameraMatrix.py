import numpy as np


class CameraMatrix:

    def __init__(self, pos, target):
        self.pos = np.array(pos)
        self.target = np.array(target)
        self.up = np.array([0, 1, 0])
        self.cz = np.subtract(self.pos, self.target)/float(np.linalg.norm(np.subtract(self.pos, self.target)))
        self.cx = np.cross(self.up, self.cz)/float(np.linalg.norm(np.cross(self.up, self.cz)))
        self.cy = np.cross(self.cx, self.cz)/float(np.linalg.norm(np.cross(self.cx, self.cz)))
        r1 = np.append(self.cx, np.array(np.dot(self.cx, self.pos)))
        r2 = np.append(self.cy, np.array(np.dot(self.cy, self.pos)))
        r3 = np.append(self.cz, np.array(np.dot(self.cz, self.pos)))
        r4 = np.array([0, 0, 0, 1])
        self.matrix = np.vstack((r1, r2, r3, r4))
