import numpy as np


mu = np.array([[1], [2], [3]])
sigma = np.array([[3, -1, 1], [-1, 5, 3], [1, 3, 4]])

Z = np.random.randn(3)
A = np.linalg.cholesky(sigma)
X = mu + np.dot(A, Z.T)

print(X)








