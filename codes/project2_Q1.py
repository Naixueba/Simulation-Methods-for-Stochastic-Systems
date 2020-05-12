# Question 1
import numpy as np
import matplotlib.pyplot as plt


# part (a)
N = 1000     # switch N among: 100, 500, 1000
samples = np.random.uniform(-3, 2, N)
counts, bins, ignored = plt.hist(samples, edgecolor='black', alpha=0.75)

plt.figure(1)
plt.title("Histogram of {} Uniformly Distributed Samples".format(N))
plt.xlabel("Sample Values")
plt.ylabel("Frequency")
plt.show()


# part (b)
sample_mean = np.mean(samples)
sample_variance = np.var(samples)

print("sample mean = {} and sample variance = {}".format(sample_mean, sample_variance))


# part (c)
from sklearn.utils import resample


N_resample = 1000       # number of resample
std = []
mean = []

# re-sample, compute corresponding mean & std, and store them
for i in range(N_resample):
    re_samples = resample(samples, n_samples=len(samples), replace=True)

    mean.append(np.mean(re_samples))
    std.append(np.std(re_samples))

# sort mean and std
mean = np.sort(mean)
std = np.sort(std)


# compute 95% confidence interval
a = 95
per_1_mean = np.percentile(mean, (100-a)/2, interpolation='nearest')
per_2_mean = np.percentile(mean, (100+a)/2, interpolation='nearest')
print('The ', str((100-a)/2), '% percentile mean is: ', str(per_1_mean))
print('The ', str((100+a)/2), '% percentile mean is: ', str(per_2_mean))

per_1_std = np.percentile(std, (100-a)/2, interpolation='nearest')
per_2_std = np.percentile(std, (100+a)/2, interpolation='nearest')
print('The ', str((100-a)/2), '% percentile std is: ', str(per_1_std))
print('The ', str((100+a)/2), '% percentile std is: ', str(per_2_std))


# plot
plt.figure(2)
bins = np.arange(min(mean) - 0.1, max(mean)+0.1, 0.02)
plt.hist(mean, bins, edgecolor='black', alpha=0.75)
plt.title("Bootstrap Confidence Interval for Sample Mean")
plt.ylabel("Frequency")
plt.xlabel("Sample Means")
plt.show()

plt.figure(3)
bins = np.arange(min(std) - 0.1, max(std)+0.1, 0.01)-0.5
plt.hist(std, bins, edgecolor='black', alpha=0.75)
plt.title("Bootstrap Confidence Interval for Sample Deviation")
plt.ylabel("Frequency")
plt.xlabel("Sample Deviations")
plt.show()



