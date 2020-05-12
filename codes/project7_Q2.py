import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# x range
xrange = np.linspace(-6, 6, 1000)

# theoretical p.d.f.
theo = 0.4*np.array(norm(-1, 1).pdf(xrange)) + 0.6*np.array(norm(1, 1).pdf(xrange))

# sampling
p = 0.4
data = []
N = 1000
for i in range(N):
    if np.random.rand() < 0.4:
        data.append(np.random.normal(-1, 1))
    else:
        data.append(np.random.normal(1, 1))


# plot
plt.figure()
plt.hist(data, bins=50, density=1, label='random samples', alpha=0.75)
plt.plot(xrange, theo.tolist(), label='theoretical', color='r')
plt.legend()
plt.savefig('Q2_{}.png'.format(N))
plt.show()








