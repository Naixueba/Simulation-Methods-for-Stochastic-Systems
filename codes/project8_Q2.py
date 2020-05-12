import numpy as np


# part (a)
N = 100
Expectation_hist = []

for trails in range(N):
    # define initial x
    x = [[5], [5], [5]]

    # simulation in 1 trial
    for i in range(1000):
        sum = 0
        temp = 0
        randint = np.random.randint(3)

        for j in range(3):
            if j == randint:
                continue
            sum += (j+1) * x[j][-1]

        # define the rest of (15-sum)
        rest = 15 - sum

        # generate one random variable
        while temp * (randint+1) <= rest:
            temp = np.random.exponential(1)
        x[randint].append(temp)

    # averaged x
    Expectation_hist.append(np.mean(np.mean(x[0]) + 2*np.mean(x[1]) + 3*np.mean(x[2])))

print('The averaged Expectation in {} trails is: {}'.format(N, np.mean(Expectation_hist)))


# part (b)
Expectation_hist_b = []

for trails in range(N):
    # define initial x
    x_b = [[0.33], [0.33], [0.33]]

    # simulation in 1 trial
    for i in range(100):
        sum = 0
        temp = 0
        randint = np.random.randint(3)

        for j in range(3):
            if j == randint:
                continue
            sum += (j+1) * x_b[j][-1]

        # define the rest of (1-sum)
        rest = 1 - sum

        # generate one random variable
        while temp * (randint+1) > rest:
            temp = np.random.exponential(1)
        x_b[randint].append(temp)

    # averaged x
    Expectation_hist_b.append(np.mean(np.mean(x_b[0]) + 2*np.mean(x_b[1]) + 3*np.mean(x_b[2])))

print('The averaged Expectation in {} trails is: {}'.format(N, np.mean(Expectation_hist_b)))



