import numpy as np

a = []
b = np.zeros((5,), dtype=np.int)
kind = 1
b[kind] = 1
for i in range(0,10):
    a.append(b)
print str(a)
