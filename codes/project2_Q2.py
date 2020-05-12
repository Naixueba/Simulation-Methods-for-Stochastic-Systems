import numpy as np


# part (a)
N = 100
X = np.random.uniform(0, 1, N+1)        # generate n uniformly distributed samples

X_k = X[:N]                             # samples of: 0 ~ N
X_k_plus_1 = X[1:]                      # samples of: 1 ~ N+1

cov = np.sum((X_k - np.mean(X_k)) * (X_k_plus_1 - np.mean(X_k_plus_1))) / N
corr = cov / (np.std(X_k) * np.std(X_k_plus_1))
print('the covariance between Xk and Xk+1 is: {}'.format(cov))
print('the correlation between Xk and Xk+1 is: {}'.format(corr))


# part (b)
X_k_minus_1 = X[:N-1]
X_k_minus_2 = X[:N-2]
X_k_minus_3 = X[:N-3]

X_k_minus_1 = np.insert(X_k_minus_1, 0, [0])        # padding 0
X_k_minus_2 = np.insert(X_k_minus_2, 0, [0, 0])
X_k_minus_3 = np.insert(X_k_minus_3, 0, [0, 0, 0])

Y = X_k - 2*X_k_minus_1 + 0.5*X_k_minus_2 - X_k_minus_3

cov_XY = np.sum((X_k-np.mean(X_k)) * (Y-np.mean(Y))) / N
corr_XY = cov_XY / (np.std(X_k) * np.std(Y))
print('the covariance between XK and Yk is: {}'.format(cov_XY))
print('the correlation between Xk and Yk is: {}'.format(corr_XY))


