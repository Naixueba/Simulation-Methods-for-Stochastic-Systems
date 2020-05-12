import numpy as np
import matplotlib.pyplot as plt


# compute the value of p
sum_ = 0
for i in range(1, 61):
    sum_ += (1 / i)
p = 1 / sum_


# sampling from N60
history = []
N = 10000
for i in range(N):
    count = 0
    while True:
        x = np.random.uniform(0, 1)
        count += 1
        if x < p/60:
            history.append(count)
            break

print('p={}'.format(p))
print('E[60] = {}'.format(np.mean(history)))
print('V[60] = {}'.format(np.var(history)))

# plot
plt.figure(1)
bins = np.arange(min(history)-1, max(history)+2) - 0.5
plt.hist(history, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of N60')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()




