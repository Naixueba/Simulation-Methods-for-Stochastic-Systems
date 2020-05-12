import numpy as np
import matplotlib.pyplot as plt


N = 1000
r_ij = 0.5
# r = [0.5, 0.5]            # part (a)
r = [0.75, 0.25]            # part (b)


output1_hist = []
output2_hist = []


for p in np.arange(0, 1, 0.01):
    buffer1 = 0; buffer2 = 0
    output1 = 0; output2 = 0

    for trail in range(N):
        if np.random.uniform() < r_ij:
            buffer1 += 1
        if np.random.uniform() < r_ij:
            buffer2 += 1

        # buffer a && buffer 2
        if buffer1 > 0 and buffer2 > 0:
            select1 = np.random.uniform()
            select2 = np.random.uniform()

            if select1 < r[0] and select2 < r[0]:
                output1 += 1
                if np.random.uniform() < r_ij:
                    buffer1 -= 1
                else:
                    buffer2 -= 1

            elif select1 >= r[0] and select2 >= r[0]:
                output2 += 1
                if np.random.uniform() < r_ij:
                    buffer1 -= 1
                else:
                    buffer2 -= 1

            else:
                output1 += 1; buffer1 -= 1
                output2 += 1; buffer1 -= 1

        # buffer 1
        elif buffer1 > 0:
            buffer1 -= 1
            if np.random.uniform() < r[0]:
                output1 += 1
            else:
                output2 += 1

        # buffer 2
        elif buffer2 > 0:
            buffer2 -= 1
            if np.random.uniform() < r[0]:
                output1 += 1
            else:
                output2 += 1

    output1_hist.append(output1 / N)
    output2_hist.append(output2 / N)

# plot
plt.figure(1)
x = np.arange(0, 1, 0.01)
plt.plot(x, output1_hist)
plt.xlabel('Probability of Packet Arrival')
plt.ylabel('Number of Packet Arrives at Input 1')
plt.show()

plt.figure(2)
plt.plot(x, output2_hist)
plt.xlabel('Probability of Packet Arrival')
plt.ylabel('Number of Packet Arrives at Input 2')
plt.show()


