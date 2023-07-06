import numpy as np

#Егор
def soprGradMethod(A: np.ndarray,
  b: np.ndarray,
  eps: np.float64) -> np.float64:
  
    n = b.size
    x = np.ones(n)
    r = np.dot(A, x) - b
    p = - r
    r_k_norm = np.dot(r, r)
    r_k_0 = r_k_norm
    for i in range(2*n):
        Ap = np.dot(A, p)
        alpha = r_k_norm / np.dot(p, Ap)
        x += alpha*p
        r += alpha*Ap
        r_kplus1_norm = np.dot(r, r)
        beta = r_kplus1_norm / r_k_norm
        r_k_norm = r_kplus1_norm
        if np.sqrt(r_kplus1_norm)/np.sqrt(r_k_0) < eps:
            break
        p = beta*p - r
    return x
