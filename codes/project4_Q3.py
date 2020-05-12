import numpy as np
import random


# load data
data = np.loadtxt('faithful.dat.txt', skiprows=26)
data = data[:, 2]
data_15 = data[0:15]

data = list(data)
data_15 = list(data_15)


def statistical_CI(data_):
    mean = np.mean(data_)
    std = np.std(data_, ddof=1)
    z = 1.96
    return [mean - z*(std/np.sqrt(len(data_))), mean + z*(std/np.sqrt(len(data_)))]


def bootstrap_CI(data_):
    sample_mean_history = []
    for i in range(1000):
        samples = []
        for j in range(len(data_)):
            samples.append(random.sample(data, 1))
        sample_mean_history.append(np.mean(samples))
    return [np.percentile(sample_mean_history, 2.5), np.percentile(sample_mean_history, 97.5)]


def run_15(data_):
    lower, upper = statistical_CI(data_)
    print('95% Statistical C.I. for 15 data: lower bound: {}; upper bound: {}'.format(lower, upper))
    lower, upper = bootstrap_CI(data_)
    print('95% Bootstrap C.I. for 15 data: lower bound: {}; upper bound: {}'.format(lower, upper))


def run_all(data_):
    lower, upper = statistical_CI(data_)
    print('95% Statistical C.I. for all data: lower bound: {}; upper bound: {}'.format(lower, upper))
    lower, upper = bootstrap_CI(data_)
    print('95% Bootstrap C.I. for all data: lower bound: {}; upper bound: {}'.format(lower, upper))


# run
run_15(data_15)
run_all(data)


# output
# 95% Statistical C.I. for 15 data: lower bound: 63.278770830413194; upper bound: 78.58789583625348
# 95% Bootstrap C.I. for 15 data: lower bound: 63.666666666666664; upper bound: 77.535
# 95% Statistical C.I. for all data: lower bound: 69.28139874542947; upper bound: 72.51271890162934
# 95% Bootstrap C.I. for all data: lower bound: 69.19806985294117; upper bound: 72.46700367647058


