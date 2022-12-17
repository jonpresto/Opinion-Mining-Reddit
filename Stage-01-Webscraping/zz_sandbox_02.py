import numpy as np

min = 1
max = 0
for i in range(300):
    r = 4*np.random.rand()
    alpha = 10**r
    print(i, ":   ", alpha)
    if alpha > max:
        max = alpha
    if alpha < min:
        min = alpha

print("max: ", max)
print("min: ", min)