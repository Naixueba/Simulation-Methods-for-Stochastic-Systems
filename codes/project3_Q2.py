import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import comb


lamda = 120         # lambda of Poisson
trails = 1000       # number of simulation times
N = 5000           # number of small time intervals
p = lamda / N       # p in Bernoulli


# theoretical poisson pmf
p_pmf_range = range(lamda-40, lamda+40)
P_pmf = stats.poisson.pmf(p_pmf_range, lamda)


# theoretical bernoulli pmf
b_pmf_range = np.arange(lamda-40, lamda+40, 1)
B_pmf = [comb(N, k) * pow(p, k) * pow(1-p, N-k) for k in b_pmf_range]


# Poisson Samples
P_history = np.random.poisson(lamda, trails)

plt.figure(1)
bins = np.arange(80, 160, 5)
plt.hist(P_history, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of Poisson Samples')
plt.xlabel('Number of Cars')
plt.ylabel('Frequency')
ax = plt.twinx()
ax.plot(p_pmf_range, P_pmf, color='r', label='theoretical poisson pmf')
plt.legend()
plt.show()


# Bernoulli Approximation
B_history = []

for i in range(trails):
    u = np.random.rand(N, 1)
    bernoulliTrails = u < p
    B_history.append(np.sum(bernoulliTrails))

plt.figure(2)
bins = np.arange(80, 160, 5)
plt.hist(B_history, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of Bernoulli Samples')
plt.xlabel('Number of Cars')
plt.ylabel('Frequency')
ax = plt.twinx()
ax.plot(b_pmf_range, B_pmf, color='r', label='theoretical binomial pmf')
plt.legend()
plt.show()

