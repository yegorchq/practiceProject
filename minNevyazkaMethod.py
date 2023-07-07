import numpy as np

def minNevyazkaMethod(A, b, eps):

    m = b.size
    x = np.zeros(m)
    y = np.zeros(m)
    y = A@x - b
    y0 = y
    #while (linalg.norm(A@x - b, ord = 2)/linalg.norm(b, ord = 2)) >= eps:
    while (np.sqrt(np.dot(y, y)/np.dot(y0, y0))) >= eps:
        t = np.sum((A@y)*y)/np.sum((A@y)*(A@y))
        x -= (t*y)
        y = A@x - b
    return x
