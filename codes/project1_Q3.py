import numpy as np
import matplotlib.pyplot as plt


N_flips = 100
N_heads = 0
history = np.empty([N_flips, 1])
longest_heads = 0
length_of_heads_run = []

# generate coin-flip sequence
for i in range(0, N_flips):
    if np.random.random() >= 0.5:       # fair coin
        N_heads += 1
        history[i] = 1
    else:
        history[i] = 0

# record the length of heads run
temp = 0
for i in range(0, N_flips-1):
    if history[i+1] == 1:
        temp += 1
    else:
        length_of_heads_run.append(temp)
        temp = 0


# plot
plt.figure(1)
bins = np.arange(8) + 0.5
plt.hist(length_of_heads_run, bins, edgecolor="b", alpha=0.75)
plt.title("The result of tossing a fair coin 100 times")
plt.xlabel("tail = 0, head = 1")
plt.ylabel("length of heads run")
plt.show()

