#Стефан
import numpy as np
def relaxationMethod(A, b, eps):
  for i in range(A.shape[0]):
      row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]

  x = np.zeros_like(b)
  n = b.size
  x0 = np.ones_like(b)
  
  for it_count in range(1, 20*n):
      x_new = np.zeros_like(x)
      for i in range(A.shape[0]):
          s1 = np.dot(A[i, :i], x_new[:i])
          s2 = np.dot(A[i, i + 1:], x[i + 1:])
          x_new[i] = (b[i] - s1 - s2) / A[i, i]
      if (np.sqrt(np.dot(x_new, x_new)/np.dot(x0, x0))) >= eps:
          break
      if (it_count == 2):
        x0 = x_new
      x = x_new

    return x