import math
import random
import matplotlib.pyplot as plt
import scipy.stats
import matplotlib.animation as animation
import numpy as np
from scipy import stats


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
ecf_x = np.sort(return_y1)
ecf_y = np.arange(len(ecf_x)) / float(len(ecf_x))
plt.plot(ecf_x, ecf_y, label=f'period = {period_x1}')

period_x2 = n+5
return_y2 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x2)
    return_y2.append(math.log(total1 / r1))

ecf_x2 = np.sort(return_y2)
ecf_y2 = np.arange(len(ecf_x2)) / float(len(ecf_x2))
plt.plot(ecf_x2, ecf_y2, label=f'period = {period_x2}')

period_x3 = n+10
return_y3 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x3)
    return_y3.append(math.log(total1 / r1))

ecf_x3 = np.sort(return_y3)
ecf_y3 = np.arange(len(ecf_x3)) / float(len(ecf_x3))
plt.plot(ecf_x3, ecf_y3, label=f'period = {period_x3}')
plt.title(f'Empirical Cumulative Distribution for period = {period_x1}, {period_x2}, {period_x3} when R = {r1}')
plt.legend(loc="lower right")
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")

reference_line_1_x = [0, 10]
reference_line_1_y = [1.0, 1.0]
plt.plot(reference_line_1_x, reference_line_1_y, '--', color="black")

plt.show()
