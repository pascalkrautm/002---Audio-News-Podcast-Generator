n = 4
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)

import numpy as np
m = np.reshape(range(16), (4, 4))
print(m * 2)