import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg


#метод наискорейшего спуска
<<<<<<< HEAD
def MetodNaiscorSp(A, b, eps):
    x = np.zeros(np.size(b))
    y = np.zeros(np.size(b))
    y = A@x - b
    while np.sqrt(np.dot(A@x - b, A@x - b)/np.dot(b, b)) >= eps:
        t = np.dot(y, y)/np.dot(A@y, y)
        x -= (t*y)
        y = A@x - b
    return x
=======
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
>>>>>>> ef730fce0422517dfcc5ad3a80418d8a8cd7a1c3
