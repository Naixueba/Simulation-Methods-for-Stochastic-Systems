import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt


N = 100         # number of individuals
n = 500         # number of steps to take


# define initial input

# all of the N individuals are diploid heterozygous, i.e. P(100-A1, 100-A2) = 1
# input = np.zeros((1, 2*N))
# input = np.insert(input, 100, 1)

input = np.zeros((1, 2*N))
input = np.insert(input, 50, 1)     # change the initial allele distributions
# input = np.insert(input, 80, 0.25)     # change the initial allele distributions
# input = np.insert(input, 120, 0.25)     # change the initial allele distributions
# input = np.insert(input, 160, 0.25)     # change the initial allele distributions


# M.C. transition matrix
P = np.zeros((2*N+1, 2*N+1))
for i in range(0, 2*N+1):
    for j in range(0, 2*N+1):
        P[i][j] = comb(2*N, j, exact=True, repetition=False) * (i/(2*N)) ** j * (1 - i/(2*N)) ** (2*N - j)


# output
output = np.zeros((n+1, 2*N+1))
output[0, :] = input            # generate first output value by copy input value to 1st row
t = np.arange(0, n)

for i in range(1, n):
    output[i, :] = np.dot(output[i-1, :], P)
    if np.allclose(output[i, :], output[i-1, :]):
        print('Convergence after ' + str(i), 'iterations')
        print(output[i, :])
        break


plt.figure(1)
x = np.arange(0, 2*N+1, 1)
plt.plot(x, output[n-1, :])
plt.title('After n = {} Steps'.format(n))
plt.ylabel('Alleles Distribution')
plt.xlabel('More A1 <------         ------> More A2')
plt.savefig('Q3_n_{}_501'.format(n))
plt.show()

