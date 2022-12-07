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

def test_game(repetition):
    t_x = 5
    t_y = []
    total = 0
    for j in range(repetition):
        total += game(t_x)
        t_y.append(total / repetition)
    return t_x, t_y

repeat = 100
n_for_median = repeat
r1 = 256

x21, y21 = test_game(r1)
y_1 = np.array([y21])
for i in range(n_for_median):
    if i % 100 == 0: print(i, 'asd')
    x21, y21 = test_game(r1)

period_x1 = 10
return_y1 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x1)
    return_y1.append(math.log(total1 / r1))

plt.figure(1)
ecf_x = np.sort(return_y1)
ecf_y = np.arange(len(ecf_x)) / float(len(ecf_x))
plt.plot(ecf_x, ecf_y, label='period = 10')

period_x2 = 15
return_y2 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x2)
    return_y2.append(math.log(total1 / r1))

ecf_x2 = np.sort(return_y2)
ecf_y2 = np.arange(len(ecf_x2)) / float(len(ecf_x2))
plt.plot(ecf_x2, ecf_y2, label='period = 15')

period_x3 = 20
return_y3 = []
for i in range(10000):
    total1 = 0
    for j in range(r1):
        total1 += game(period_x3)
    return_y3.append(math.log(total1 / r1))

ecf_x3 = np.sort(return_y3)
ecf_y3 = np.arange(len(ecf_x3)) / float(len(ecf_x3))
plt.plot(ecf_x3, ecf_y3, label='period = 20')
plt.title(f'Empirical Cumulative Distribution for period = 10, 15, 20 when R={r1}')
plt.legend(loc="lower right")
plt.xlabel("ln(average payoff)")
plt.ylabel("frequency")

reference_line_1_x = [0, 8]
reference_line_1_y = [1.0, 1.0]
plt.plot(reference_line_1_x, reference_line_1_y, '--', color="black")

plt.show()
