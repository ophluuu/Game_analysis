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


def repeat_game(repetition_number):
    x = [i for i in range(1, 51, 1)]
    y = []
    for i in x:
        total = 0
        for j in range(repetition_number):
            total += game(i)
        y.append(total / repetition_number)
    return x, y


if __name__ == '__main__':
    repeat = 100
    n_for_median = repeat
    r1 = 512

    x11, y11 = repeat_game(r1)
    y1 = np.array([y11])
    for i in range(n_for_median):
        if i % 100 == 0: print(i)
        x11, y11 = repeat_game(r1)
        y1 = np.vstack([y1, y11])

    percent1 = 5
    percent2 = 95

    ymedian1 = np.median(y1, axis=0)
    y161 = np.percentile(y1, percent1, axis=0)
    y841 = np.percentile(y1, percent2, axis=0)

    ymean = np.mean(y1, axis=0)
    plt.plot(x11, y161, label=f"{percent1} percentile")
    plt.plot(x11, ymedian1, label="median")
    #plt.plot(x11, ymean, label=f"mean for {repeat} trials")
    plt.plot(x11, y841, label=f"{percent2} percentile")
    # x21, y21 = repeat_game(r2)
    # y2 = np.array([y21])
    # for i in range(n_for_median-1):
    #    print(i)
    #    x21, y21 = repeat_game(r2)
    #    y2 = np.vstack([y2, y21])
    # ymedian2 = np.median(y2, axis=0)
    # plt.plot(x21, ymedian2, label="R = 2^5 = 32")

    expectedx = [i for i in range(1, 51)]
    expectedy = [i / 2 + 0.5 for i in expectedx]
    plt.plot(expectedx, expectedy, label="expected value")

    reference_line_1_x = [10, 10]
    reference_line_1_y = [0, 5.5]
    plt.plot(reference_line_1_x, reference_line_1_y, '--', color="black")

    reference_line_2_x = [1, 10]
    reference_line_2_y = [5.5, 5.5]
    plt.plot(reference_line_2_x, reference_line_2_y, '--', color="black")

    plt.title(f"Median Average Return for Sample of {r1} Trials, repeat= {repeat}")
    plt.xlabel("number of game period")
    plt.ylabel("return")
    plt.legend(loc="upper left")

    plt.xticks([x for x in expectedx if x % 5 == 0])

    plt.show()
    '''
    ima = expectedy-ymedian1
    plt.plot([i for i in range(1, 21)], ima[:20])
    plt.title(f"expected value - median for R = {r1}")
    plt.show()
    '''

