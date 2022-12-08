import math
import random
import matplotlib.pyplot as plt
import scipy.stats
import matplotlib.animation as animation
import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

def test():
    if random.random() > 0.5:
        return True
    else:
        return False


def game(period):
    retur = 1
    count = 0
    while test() and count < (period - 1):
        retur *= 2
        count += 1
    return retur


n = 6
r1 = 2**(n-1)


period_x1 = n
return_y1 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x1)
    return_y1.append(math.log(total1 / r1))

plt.figure(1)
ecf_x1 = np.sort(return_y1)
ecf_y1 = np.arange(len(ecf_x1)) / float(len(ecf_x1))
plt.plot(ecf_x1, ecf_y1)
plt.title(f'Empirical Cumulative Distribution for R={r1}, period = {period_x1}, replication = 10000')
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")

plt.figure(2)
plt.hist(return_y1, bins=100)
plt.xlim([0, 8])
plt.title(f'Probability Density Function for R={r1}, period = {period_x1}, replication = 10000')
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")

period_x2 = n+5
return_y2 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x2)
    return_y2.append(math.log(total1 / r1))

plt.figure(3)
ecf_x2 = np.sort(return_y2)
ecf_y2 = np.arange(len(ecf_x2)) / float(len(ecf_x2))
plt.plot(ecf_x2, ecf_y2)
plt.title(f'Empirical Cumulative Distribution for R={r1}, period = {period_x2}, replication = 10000')
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")

plt.figure(4)
plt.hist(return_y2, bins=100)
plt.xlim([0, 8])
plt.title(f'Probability Density Function for R={r1}, period = {period_x2}, replication = 10000')
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")


period_x3 = n+10
return_y3 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x3)
    return_y3.append(math.log(total1 / r1))

plt.figure(5)
ecf_x3 = np.sort(return_y3)
ecf_y3 = np.arange(len(ecf_x3)) / float(len(ecf_x3))
plt.plot(ecf_x3, ecf_y3)
plt.title(f'Empirical Cumulative Distribution for R={r1}, period = {period_x3}, replication = 10000')
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")

plt.figure(6)
plt.hist(return_y3, bins=100)
plt.xlim([0, 8])
plt.title(f'Probability Density Function for R={r1}, period = {period_x3}, replication = 10000')
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")
plt.show()
