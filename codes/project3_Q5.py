import numpy as np
import matplotlib.pyplot as plt


p = np.array([0.06, 0.06, 0.06, 0.06, 0.06, 0.15, 0.13, 0.14, 0.15, 0.13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
N = 10000
X = []

c = 3       # c = max(p) / min(q) = 0.15 / 0.05 = 3

for i in range(1, N):
    while True:
        j = int(1 + np.floor(20*np.random.rand()))      # get uniform j from {1, 2, ..., 20}
        if (c*np.random.rand()) < p[j-1]/0.05:
            X.append(j)
        break

print('Mean of X: {}'.format(np.mean(X)))
print('Efficiency = {}'.format(len(X)/N))

plt.figure(1)
plt.hist(X, bins=range(21), edgecolor='black', alpha=0.75, label='Accept-Reject Method')
plt.plot(range(1, 21), [x*N/c for x in p], marker='o', color='red', label='Distribution of Pj')
plt.title('Histogram of Distribution of P')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
