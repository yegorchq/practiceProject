import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg


#метод наискорейшего спуска
def MetodNaiscorSp(A, b, eps):
    x = np.zeros(np.size(b))
    y = np.zeros(np.size(b))
    y = A@x - b
    while (linalg.norm(A@x - b, ord = 2)/linalg.norm(b, ord = 2)) >= eps:
        t = np.sum(y*y)/np.sum((A@y)*y)
        x -= (t*y)
        y = A@x - b
    return x
