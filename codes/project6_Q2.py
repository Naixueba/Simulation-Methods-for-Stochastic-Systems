import numpy as np
import matplotlib.pyplot as plt


N = 10000
k = 5.5
theta = 1


def f(x, k, theta):
    value = (2 / (np.sqrt(np.pi)*4.5*3.5*2.5*1.5)) * (1/(theta**k)) * (x**(k-1)) * np.exp(-x/theta)
    return value


def g(y):
    value = (1/k) * np.exp(-y/k)
    return value


result = []
theo = []
accept_num = 0

# use accept-reject to generate
for i in range(N):
    u = -k * np.log(np.random.uniform())
    if np.random.uniform() < f(u, k, theta)/(np.e*g(u)):
        result.append(u)
        accept_num += 1

# theoretical sequence
xrange = np.arange(0, 30, 0.01)
for y in xrange:
    theo.append(f(y, k, theta))


# result & plot
print('Acceptance Rate = %.2f' % (accept_num / N))
plt.figure()
plt.hist(result, bins=30, edgecolor='black', alpha=0.75, density=1, label='Simulation')
plt.plot(xrange, theo, color='r', alpha=0.75, label='theoretical')
plt.ylabel('Frequency')
plt.xlabel('X')
plt.legend()
plt.savefig('Q2_a')
plt.show()


