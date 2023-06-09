import numpy as np


class VTensor:

    def __init__(self, corner, dim):
        self.corner = np.array(corner)  # array [x, y, z]
        self.value = np.zeros(np.flip(dim))  # array [[[ 0, ... , 0 ]]]

    def __getitem__(self, key):
        fkey = tuple(np.flip(key))
        return self.value[fkey]

    def __setitem__(self, key, value):
        fkey = tuple(np.flip(key))
        self.value[fkey] = value

    def __str__(self):
        return "{" + str(self.corner) + ",\n" + str(np.flip(self.value, axis=0)) + "}"

    @property
    def dim(self):
        return tuple(np.flip(self.value.shape))

    @property
    def oppCorner(self):
        return self.corner + self.dim - 1

    def pointToGlobal(self, point):
        return point + self.corner

    def pointToLocal(self, point):
        return point - self.corner

    @staticmethod
    def union(T1, T2):
        corner = np.vstack((T1.corner, T2.corner)).min(axis=0)
        dim = np.vstack((T1.oppCorner, T2.oppCorner)).max(axis=0) - corner + 1
        res = VTensor(corner, dim)

        for point in np.ndindex(T1.dim):
            res[res.pointToLocal(T1.pointToGlobal(point))] += T1[point]

        for point in np.ndindex(T2.dim):
            res[res.pointToLocal(T2.pointToGlobal(point))] += T2[point]

        return res


t1 = VTensor(corner=(2,2), dim=(4,3))
t1.value += 1
print("T1 =", t1, end="\n\n")

t2 = VTensor(corner=(7,4), dim=(2,2))
t2.value += 2
print("T2 =", t2, end="\n\n")

t3 = VTensor.union(t1, t2)
print("T3 =", t3, end="\n\n")


