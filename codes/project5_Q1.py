import numpy as np


N = 100                             # number of simulations
break_time_hist = np.zeros(N)       # record the total break time of each simulation
rate = [4, 7, 10, 13, 16, 19, 19, 16, 13, 10, 7]    # rate of the non-homogeneous poisson process


for trail in range(N):
    # generate arrival time sequence
    arrival_time = []

    for hour in range(100):
        time = hour
        while True:
            u = np.random.uniform()
            lamda = rate[hour % 10]
            time -= (1/lamda) * np.log(u)
            if time - hour > 1:
                break
            arrival_time.append(time)

    # serve the job and break...
    break_time = []
    time_point = 0

    while len(arrival_time):
        if arrival_time[0] > time_point:
            break_time.append(np.random.uniform(0, 0.3))
            time_point += break_time[-1]

        else:
            time_point += np.random.exponential(1/25)
            arrival_time.remove(arrival_time[0])

    break_time_hist[trail] = sum(break_time)


# print results
print(break_time_hist)
print('The expected break time is %.2f' % np.mean(break_time_hist))
print('The std is %.3f' % np.std(break_time_hist))

