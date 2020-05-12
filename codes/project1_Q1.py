import numpy as np
import matplotlib.pyplot as plt


N_flips = 50
N_heads = 0
history = np.empty([N_flips, 1])
longest_heads = 0

# generate coin-flip sequence
for i in range(0, N_flips):
    if np.random.random() >= 0.5:       # fair coin
        N_heads += 1
        history[i] = 1

    else:
        history[i] = 0

# check the longest run of heads
temp = 0
for i in range(0, N_flips-1):
    if history[i+1] == 1:
        temp += 1
        if temp > longest_heads:
            longest_heads = temp
    else:
        temp = 0

# print results
print("Number of heads is {}".format(N_heads))
print("The longest run of heads is {}".format(longest_heads))

# plot
plt.figure(1)
bins = np.arange(3) - 0.5
plt.hist(history, bins, edgecolor="b", alpha=0.75)
plt.title("The result of tossing a fair coin 50 times")
plt.xlabel("tail = 0, head = 1")
plt.ylabel("counts")
plt.show()


# repeat the experiment for 20 times
N_repeat = 20    # 20, 100, 200, 1000; switch the number to generate different results
N_heads_hist = np.empty(N_repeat)

for i in range(0, N_repeat):
    N_heads = 0
    for j in range(0, N_flips):
        if np.random.random() >= 0.5:
            N_heads += 1
            history[j] = 1
        else:
            history[j] = 0
    N_heads_hist[i] = N_heads

# plot
plt.figure(2)
bins = np.arange(N_flips+1) - 0.5
plt.hist(N_heads_hist, bins, edgecolor='b', alpha=0.75)
plt.xticks(range(51))
plt.xlim(10, 40)
plt.title("The histogram of repeating the experiment {} times".format(N_repeat))
plt.xlabel("tail = 0, head = 1")
plt.ylabel("number of heads")
plt.show()





