import numpy as np

goal = np.array([30.390625, 13.984375, 4.453125, 16.015625, 7.578125, 20.859375, 6.71875]) / 100
lst = np.zeros(7)
n = 0


def regress():
    return (goal - lst / n).argmax()


while not all(goal == (lst / n)):
    ind = regress()
    lst[ind] += 1
    n += 1
    if not n % 10:
        print(n)
        print(lst / n)
print(n)
