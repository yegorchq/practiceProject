import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg


#метод наискорейшего спуска
def minResMeth(A, b, eps):
    it = 0
    x = np.zeros(m)
    y = np.zeros(m)
    y = A@x - b
    while (linalg.norm(A@x - b, ord = 2)/linalg.norm(b, ord = 2)) >= eps:
        t = np.sum(y*y)/np.sum((A@y)*y)
        x -= (t*y)
        y = A@x - b
        it += 1
    return x, it
