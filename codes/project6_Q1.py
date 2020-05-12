import numpy as np
import matplotlib.pyplot as plt
import time


# Box-Muller Method
# start_box = time.time()
N = 1000
X_mean = 1; X_var = 4
Y_mean = 2; Y_var = 9

u1 = np.random.rand(N, 1)
u2 = np.random.rand(N, 1)

# generate X and Y that are N(0,1) random variables and independent
X = np.sqrt(-2*np.log(u1)) * np.cos(2*np.pi*u2)
Y = np.sqrt(-2*np.log(u1)) * np.sin(2*np.pi*u2)

# scale them to particular mean and variance
x = X_mean + np.sqrt(X_var)*X       # x ~ N(X_mean, X_var)
y = Y_mean + np.sqrt(Y_var)*Y       # y ~ N(X_mean, X_var)
A = x + y

# print time
# end_box = time.time()


# compute cov(x, y), sample_mean, sample_variance
print('Results of Box-Muller Method')
print('Cov(x, y): {}'.format(sum((x - np.mean(x)) * (y - np.mean(y))) / N))
print('Sample mean of A: {}'.format(np.mean(A)))
print('Sample variance of A: {}\n'.format(np.var(A, ddof=1)))

# theoretical values and theoretical p.d.f
theo_pdf = []
miu = X_mean + Y_mean
delta_2 = X_var + Y_var

x_range = np.arange(min(A)-1, max(A)+1, 0.05)
for x in x_range:
    theo_pdf.append((np.exp(-(x-miu)**2 / (2*delta_2)) / np.sqrt(2*np.pi*delta_2)))


# histogram of A
plt.figure()
bins = np.arange(np.min(A), np.max(A), 1)
plt.hist(A, bins, edgecolor='black', alpha=0.75, density=1, label='Box-Muller Method')
plt.plot(x_range, theo_pdf, color='r', label='Theoretical p.d.f.', alpha=0.75)
plt.xlabel('Value of A')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('Q1_hist.png')
plt.show()


# Marsaglia's Polar method
# start_mar = time.time()

# generate X and Y that are N(0, 1)
i = 0
while i <= 999:
    u1 = 2*np.random.rand() - 1
    u2 = 2*np.random.rand() - 1
    s = u1**2 + u2**2
    if s < 1:
        X[i] = np.sqrt(-2*np.log(s)/s)*u1
        Y[i] = np.sqrt(-2*np.log(s)/s)*u2
        i += 1

# scale them
x = X_mean + np.sqrt(X_var)*X       # x ~ N(X_mean, X_var)
y = Y_mean + np.sqrt(Y_var)*Y       # y ~ N(X_mean, X_var)
A = x + y

# print time
# end_mar = time.time()


# compute covariance, sample_mean, sample_variance
print('Results of Marsaglia\'s Method')
print('Cov(x, y): {}'.format(sum((x - np.mean(x)) * (y - np.mean(y))) / N))
print('Sample mean of A: {}'.format(np.mean(A)))
print('Sample variance of A: {}\n'.format(np.var(A, ddof=1)))


# Console Results
# Results of Box-Muller Method
# Cov(x, y): [-0.014009676]
# Sample mean of A: 2.959960372120547
# Sample variance of A: 13.040561584217165
#
# Results of Marsaglia's Method
# Cov(x, y): [0.04065821]
# Sample mean of A: 3.010860622723196
# Sample variance of A: 13.227198179944219


# compare time needed to generate 1,000,000 samples
# 1. Box-Muller Method
start_box = time.time()

for i in range(1000):
    X_mean = 1; X_var = 4
    Y_mean = 2; Y_var = 9

    u1 = np.random.rand(N, 1)
    u2 = np.random.rand(N, 1)

    X = np.sqrt(-2*np.log(u1)) * np.cos(2*np.pi*u2)
    Y = np.sqrt(-2*np.log(u1)) * np.sin(2*np.pi*u2)

    x = X_mean + np.sqrt(X_var)*X       # x ~ N(X_mean, X_var)
    y = Y_mean + np.sqrt(Y_var)*Y       # y ~ N(X_mean, X_var)
    A = x + y

# print time
end_box = time.time()
print('Time Consumed for Box-Muller: %.2f s' % (end_box - start_box))


# 2. Marsaglia's Polar method
start_mar = time.time()

for j in range(1000):
    i = 0
    while i <= 999:
        u1 = 2*np.random.rand() - 1
        u2 = 2*np.random.rand() - 1
        s = u1**2 + u2**2
        if s < 1:
            X[i] = np.sqrt(-2*np.log(s)/s)*u1
            Y[i] = np.sqrt(-2*np.log(s)/s)*u2
            i += 1

    x = X_mean + np.sqrt(X_var)*X       # x ~ N(X_mean, X_var)
    y = Y_mean + np.sqrt(Y_var)*Y       # y ~ N(X_mean, X_var)
    A = x + y

# print time
end_mar = time.time()
print('Time Consumed for Marsaglia\'s: %2.f s' % (end_mar - start_mar))


# Console Results
# Time Consumed for Box-Muller: 0.11 s
# Time Consumed for Marsaglia's:  7 s

