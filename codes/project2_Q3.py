import numpy as np
import matplotlib.pyplot as plt


# part (a)
M = 10
N = 10000        # number of samples
sample = np.random.randint(0, M, N)


# plot
plt.figure(1)
bins = np.arange(0, M+1, 1) - 0.5
plt.hist(sample, bins, edgecolor="black", alpha=0.75)
plt.title("Histogram of 10000 Uniformly Distributed Samples in [0, 9]")
plt.xlabel("Sample Value")
plt.ylabel("Frequency")
plt.show()


# part (b)
from scipy.stats import chisquare
from scipy.stats import chi2


dof = M - 1     # degree of freedom
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])     # store original data
x_theo = np.array([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])     # expected = N / M = 1000

for i in range(M):
    x[i] = np.count_nonzero(sample == i)

print(x)
print(x_theo)

chi_sq_res = chisquare(x, x_theo)
print('chi square test statistic is {}'.format(chi_sq_res.statistic))
print('chi square test p-vale is: {}'.format(chi_sq_res.pvalue))
print('The 95 percentile of chi square dist with 9 dof, is: {}'.format(chi2.ppf(0.95, dof)))


# part (c)
sample_new = np.random.randint(1, M+1, N)       # generate new samples
x_new = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(M):
    x_new[i] = np.count_nonzero(sample_new == i)

print(x_new)
print(x_theo)

chi_sq_res_new = chisquare(x_new, x_theo)
print('chi square test statistic is {}'.format(chi_sq_res_new.statistic))
print('chi square test p-vale is: {}'.format(chi_sq_res_new.pvalue))
print('The 95 percentile of chi square dist with 9 dof, is: {}'.format(chi2.ppf(0.95, dof)))





