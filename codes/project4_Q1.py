import numpy as np


N = 10000       # simulation times
M = 100         # number of repeat

# part (a)
theta_a = []
for j in range(M):
    for i in range(N):
        x = np.random.uniform()
        x = 4 * np.exp(16*(x**2) - 12*x + 2)
        theta_a.append(x)
print('The result of Question1 part (a) is: {}'.format(np.mean(theta_a)))


# part (b)
theta_b = []
for j in range(M):
    for i in range(N):
        x = np.random.uniform()
        x = 2 * (np.exp(-(1/x - 1)**2) / (x**2))
        theta_b.append(x)
print('The result of Question1 part (a) is: {}'.format(np.mean(theta_b)))


# part (c)
theta_c = []
for j in range(M):
    for i in range(N):
        x = np.random.uniform()
        y = np.random.uniform()
        t = np.exp(-(x+y)**2)
        theta_c.append(t)
print('The result of Question1 part (a) is: {}'.format(np.mean(theta_c)))


# Results when M = 10
# The result of Question1 part (a) is: 92.82611069576404
# The result of Question1 part (a) is: 1.7689143095766002
# The result of Question1 part (a) is: 0.41310349770717636


# Results when M = 100
# The result of Question1 part (a) is: 92.92954773287994
# The result of Question1 part (a) is: 1.7718544002728807
# The result of Question1 part (a) is: 0.41212223311226553

