import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from scipy.stats import multivariate_normal


# part (a)
# load data
data = np.loadtxt('faithful.dat.txt', skiprows=26)
eruption = data[:, 1]
waiting = data[:, 2]
original_data = np.array([eruption, waiting]).T


# scatter plot
plt.figure(1)
plt.scatter(waiting, eruption)
plt.xlabel('waiting time')
plt.ylabel('eruption time')
plt.title('2-D Scatter Plot of Data')
plt.savefig('Q4_a_original_data.png')
plt.show()


# run k-means clustering
clusters = KMeans(n_clusters=2)
clusters.fit(original_data)


# scatter plot of clustered data
plt.figure(3)
colors = ['b', 'r']
for i, j in enumerate(clusters.labels_):
    plt.plot(waiting[i], eruption[i], color=colors[j], marker='o', ls='None')
plt.xlabel('waiting time')
plt.ylabel('eruption time')
plt.title('2-D Scatter Plot of Clustered Data')
plt.savefig('Q4_a_clustered_data.png')
plt.show()


# part (b)
# use GMM to fit original data
gmm = GaussianMixture(n_components=2, covariance_type='full')
gmm.fit(original_data)
label = gmm.predict(original_data)

mean = gmm.means_
cov = gmm.covariances_
weight = gmm.weights_


# plot contour
plt.figure()
x, y = np.mgrid[0:6:0.01, 30:110:1]
pos = np.empty(x.shape+(2,))
pos[:, :, 0] = x; pos[:, :, 1] = y

plt.contour(y, x, weight[0]*multivariate_normal.pdf(pos,mean[0,:],cov[0,:,:])
            + weight[1]*multivariate_normal.pdf(pos,mean[1,:],cov[1,:,:]))


# plot data points
for i in range(272):
    if label[i] == 0:
        plt.plot(waiting[i], eruption[i], color='r', marker='o')
    else:
        plt.plot(waiting[i], eruption[i], color='b', marker='o')

plt.title('Fit with GMM-EM Algorithm')
plt.xlabel('eruptions')
plt.ylabel('waiting')
plt.savefig('Q4_GMM.png')
plt.show()

