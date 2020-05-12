import numpy as np
import matplotlib.pyplot as plt


N = [100, 1000, 10000]
freq1 = []
freq2 = []
freq3 = []


# 100 trails
for j in range(N[0]):
    sum_ = 0
    for i in range(N[0]):
        x = np.random.uniform(0, 1)
        sum_ += x
        if sum_ > 4:
            freq1.append(i+1)
            break
# 1000 trails
for j in range(N[1]):
    sum_ = 0
    for i in range(N[1]):
        x = np.random.uniform(0, 1)
        sum_ += x
        if sum_ > 4:
            freq2.append(i+1)
            break
# 10000 trails
for j in range(N[2]):
    sum_ = 0
    for i in range(N[2]):
        x = np.random.uniform(0, 1)
        sum_ += x
        if sum_ > 4:
            freq3.append(i+1)
            break


plt.figure(1)
bins = np.arange(min(freq1)-1, max(freq1)+2) - 0.5
plt.hist(freq1, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of {} Samples'.format(N[0]))
plt.xlabel('N')
plt.ylabel('Frequency')
plt.show()

plt.figure(2)
bins = np.arange(min(freq2)-1, max(freq2)+2) - 0.5
plt.hist(freq2, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of {} Samples'.format(N[1]))
plt.xlabel('N')
plt.ylabel('Frequency')
plt.show()

plt.figure(3)
bins = np.arange(min(freq3)-1, max(freq3)+2) - 0.5
plt.hist(freq3, bins, edgecolor='black', alpha=0.75)
plt.title('Histogram of {} Samples'.format(N[2]))
plt.xlabel('N')
plt.ylabel('Frequency')
plt.show()


# print E[N]
print('When N=100, E[N]={}'.format(np.mean(freq1)))
print('When N=1000, E[N]={}'.format(np.mean(freq2)))
print('When N=10000, E[N]={}'.format(np.mean(freq3)))


