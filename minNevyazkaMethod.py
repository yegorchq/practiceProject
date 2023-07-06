#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg


# In[3]:


m = 26
beta = 572
eps = 10**(-12)

#метод минимальных невязок
def minNevyazkaMethod(A, b, eps):
    it = 0
    x = np.zeros(m)
    y = np.zeros(m)
    y = A@x - b
    while (linalg.norm(A@x - b, ord = 2)/linalg.norm(b, ord = 2)) >= eps:
        t = np.sum((A@y)*y)/np.sum((A@y)*(A@y))
        x -= (t*y)
        y = A@x - b
        it += 1
    return x, it


# In[4]:


A = np.array([[np.math.cos(i + j)/(0.1*beta) + 0.1*beta*np.math.exp(-(i-j)**2) for j in range (m)] for i in range (m)])
xh = np.array([49]*26)
b = A@xh
x, it = minNevyazkaMethod(A, b, eps)

print('x = ', x)
print('')
print('it =', it)


# In[ ]:




