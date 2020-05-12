import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from scipy.stats import multivariate_normal
import time


# define hyper-parameters
N = 300
cov_type = ['spherical', 'diag', 'full', 'tied']
label_1 = [1]*150 + [0]*150
label_2 = [0]*150 + [1]*150

# generate grid for plots
x, y = np.mgrid[-5:5:.01, -5:5:.01]
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x; pos[:, :, 1] = y


# close sub-populations
mu1 = [0, 0]; cov1 = [[2, 0], [0, 0.5]]
mu2 = [1, 1]; cov2 = [[1, 0], [0, 1]]
rv1 = multivariate_normal(mu1, cov1)
rv2 = multivariate_normal(mu2, cov2)

plt.figure()
plt.contourf(x, y, rv2.pdf(pos)+rv1.pdf(pos))
plt.title('close sub-populations')
plt.savefig('Q3_close_sub_populations.png')
plt.show()


# well-separated populations
mu3 = [-3, -3]; cov3 = [[5, 0], [0, 2]]
mu4 = [2, 2]; cov4 = [[1, 0], [0, 3]]
rv3 = multivariate_normal(mu3, cov3)
rv4 = multivariate_normal(mu4, cov4)

plt.figure()
plt.contourf(x, y, rv4.pdf(pos)+rv3.pdf(pos))
plt.title('well separated-populations')
plt.savefig('Q3_well_separated_populations.png')
plt.show()


# GMM
X1 = np.zeros((300, 2))
X1[:150, :] = np.random.multivariate_normal(mu1, cov1, size=150)
X1[150:, :] = np.random.multivariate_normal(mu2, cov2, size=150)

X2 = np.zeros((300, 2))
X2[:150, :] = np.random.multivariate_normal(mu3, cov3, size=150)
X2[150:, :] = np.random.multivariate_normal(mu4, cov4, size=150)


# spherical
start_time = time.time()
gmm = GaussianMixture(n_components=2, covariance_type='spherical')
gmm.fit(X1)
labels = gmm.predict(X1)
end_time = time.time()

plt.figure()
print('covariance type: ', cov_type[0])
print('run time:', end_time - start_time)
print('weight: ', gmm.weights_[0])
print('mean: \n', gmm.means_)
print('covariance: \n', gmm.covariances_)
print('accuracy:', max(np.mean(label_1 == labels), np.mean(label_2 == labels)))


# diag
start_time = time.time()
gmm = GaussianMixture(n_components=2, covariance_type='diag')
gmm.fit(X2)
labels = gmm.predict(X2)
end_time = time.time()

plt.figure()
print('\n -------------------------------')
print('covariance type: ', cov_type[1])
print('run time:', end_time - start_time)
print('weight: ', gmm.weights_[0])
print('mean: \n', gmm.means_)
print('covariance: \n', gmm.covariances_)
print('accuracy:', max(np.mean(label_1 == labels), np.mean(label_2 == labels)))



