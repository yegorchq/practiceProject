import numpy as np

#метод наискорейшего спуска
def MetodNaiscorSp(A, b, eps):
    x = np.zeros(np.size(b))
    y = np.zeros(np.size(b))
    y = A@x - b
    while np.sqrt(np.dot(A@x - b, A@x - b)/np.dot(b, b)) >= eps:
        t = np.dot(y, y)/np.dot(A@y, y)
        x -= (t*y)
        y = A@x - b
    return x

