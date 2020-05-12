import numpy as np


N_heads_to_reach = 100
N_flips = 0
N_heads = 0

# generate coin-flip sequence
while N_heads < N_heads_to_reach:
    if np.random.random() >= 0.5:       # fair coin
        N_heads += 1
        N_flips += 1
    else:
        N_flips += 1

# print the tossing number needed
print(N_flips)








