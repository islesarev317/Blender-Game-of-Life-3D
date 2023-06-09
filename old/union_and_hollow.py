from tensor import LocatedTensor

a = LocatedTensor.zeros(corner=(1, 1, 1), dim=(5, 4, 3))
a[1:4, 0:3] = 1
a.hollow()
#print(a)

b = LocatedTensor.zeros(corner=(3, 3, 2), dim=(3, 3, 3))
b[:] = 3
#print(b)

c = a - b
print(c)
