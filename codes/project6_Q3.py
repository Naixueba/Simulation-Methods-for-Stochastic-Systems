import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable


N = 10000
alpha = [0.5, 1.0, 1.8, 2.0]        # alpha
beta = [0, 0.75]                    # beta


def K(alpha):
    if alpha < 1:
        return alpha
    elif alpha > 1:
        return alpha - 2


def f(W, alpha, beta):
    gamma = np.random.uniform(-np.pi/2, np.pi/2)
    if alpha == 1:
        return (np.pi/2 + beta*gamma) * np.tan(gamma) - beta * np.log((W*np.cos(gamma)) / (np.pi/2 + beta*gamma))

    else:
        gamma0 = (-np.pi / 2) * beta * (K(alpha) / alpha)
        return (np.sin(alpha*(gamma-gamma0)) / (np.cos(gamma)**(1/alpha))) * ((np.cos(gamma-alpha*(gamma-gamma0)) / W)**((1-alpha)/alpha))


for a in alpha:
    for b in beta:
        x = []
        for i in range(N):
            W = np.random.exponential(1)
            x.append(f(W, a, b))

        plt.figure(figsize=(10, 6))

        # alpha-stable simulations
        plt.subplot(1, 2, 1)
        plt.hist(x, bins=100, color='black', density=1, alpha=0.75, label='Simulation: '+chr(945)+'='+str(a)+','+chr(946)+'='+str(b))
        theo = levy_stable.rvs(a, b, size=N, scale=1)
        plt.hist(theo, bins=100, color='r', density=1, label='Theoretical')
        plt.title('Simulation Histogram')
        plt.legend()

        # plots of time series
        plt.subplot(1, 2, 2)
        plt.plot(np.arange(0, N), x)
        plt.title('Time Series Plot')

        plt.savefig('Q3_a{}_b{}.png'.format(a, b))
        plt.show()



