import numpy as np
import random
import matplotlib.pyplot as plt


# part (a)
reject_hist = []
N = 1000
N_trails = 10
for j in range(N_trails):
    reject = 0
    for i in range(N):
        test_samples = random.sample(range(126), 5)
        if np.min(test_samples) <= 5:
            reject += 1
    reject_prob = reject / N
    reject_hist.append(reject_prob)

print(reject_hist)
print(np.mean(reject_hist))


# part (b)
fewest_number = []
for j in range(N_trails):           # loop to repeat the experiment several times
    reject = 0
    for i in range(6, 126):            # loop to find the fewest number, starting from 6
        reject = 0
        for k in range(N):
            test_samples = random.sample(range(126), i)     # sample i chips
            if np.min(test_samples) <= 5:
                reject += 1
        if reject >= 950:
            fewest_number.append(i)
            print(i)
            break

plt.figure(1)
bins = np.arange(min(fewest_number)-1, max(fewest_number)+2, 1) - 0.5
plt.hist(fewest_number, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of Fewest Number')
plt.ylabel('Frequency')
plt.xlabel('Fewest Number')
plt.show()




