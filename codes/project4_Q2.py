import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


N = 1000
x = []

for i in range(N):
    z1 = np.random.randn()
    z2 = np.random.randn()
    z3 = np.random.randn()
    z4 = np.random.randn()
    x.append(z1**2 + z2**2 + z3**2 + z4**2)

x = sorted(x)
t = np.arange(min(x), max(x), 0.01)
theo_cdf = stats.chi2.cdf(t, 4)

# plot
plt.figure()
plt.step(x, np.arange(1/N, 1+1/N, 1/N), label='empirical cdf')
plt.plot(t, theo_cdf, label='theoretical cdf')
plt.title('Empirical and Theoretical CDF when N = {}'.format(N))
plt.legend()
plt.show()


print('when n = {}'.format(N))
# maximum difference
max_diff = max(abs(stats.chi2.cdf(x, 4) - np.arange(1/N, 1+1/N, 1/N)))
print('max difference = {}'.format(max_diff))


# percentile
percentile = [0.25, 0.50, 0.9]
for p in percentile:
    p_emp = []
    for i in range(N):
        if (i+1)/N >= p:
            p_emp = x[i]
            break
    print('the {}th percentile of empirical is {}'.format(p, p_emp))

    p_theo = stats.chi2.ppf(p, 4)
    print('the {}th percentile of theoretical is {}'.format(p, p_theo))


# when n = 10
# max difference = 0.2263395573321131
# the 0.25th percentile of empirical is 1.4566224439688158
# the 0.25th percentile of theoretical is 1.922557526229554
# the 0.5th percentile of empirical is 2.910229780077728
# the 0.5th percentile of theoretical is 3.3566939800333224
# the 0.9th percentile of empirical is 7.176424566950743
# the 0.9th percentile of theoretical is 7.779440339734858


# when n = 100
# max difference = 0.07252711828734393
# the 0.25th percentile of empirical is 1.821696497714953
# the 0.25th percentile of theoretical is 1.922557526229554
# the 0.5th percentile of empirical is 3.496553346505567
# the 0.5th percentile of theoretical is 3.3566939800333224
# the 0.9th percentile of empirical is 7.682103514367712
# the 0.9th percentile of theoretical is 7.779440339734858


# when n = 1000
# max difference = 0.02119088123190105
# the 0.25th percentile of empirical is 1.9559444628799594
# the 0.25th percentile of theoretical is 1.922557526229554
# the 0.5th percentile of empirical is 3.299465137514017
# the 0.5th percentile of theoretical is 3.3566939800333224
# the 0.9th percentile of empirical is 7.847506922588133
# the 0.9th percentile of theoretical is 7.779440339734858

