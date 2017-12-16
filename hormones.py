"""
Secretion of hormones
"""

import math
import matplotlib.pylab as plt
from sklearn.metrics import mean_squared_error


def func(x, y, a, b, k):
    return a - b * math.cos((math.pi * x) / 12) - k * y


def func2(a, b, k, t, x):
    return a/k - b*(k/(k**2 + (math.pi/12)**2)*math.cos(math.pi*t/12) + math.pi/(12*(k**2 + (math.pi/12)**2))*math.sin(math.pi*t/12)) + math.e**(-k*t)*(x0 - a/k + b*k/(k**2 + (math.pi/12)**2))


def Euler(a, b, k, h, x, y, period):
    X, Y = [], []
    while x < period:
        y += h * func(x, y, a, b, k)
        x += h
        Y.append(y)
        X.append(x)
    return X, Y


def Analytic(a, b, k, x0, y, h, period):
    X, Y = [], []
    t = 0
    while t <= period:
        y = func2(a, b, k, t, x0)
        t = t + h
        Y.append(y)
        X.append(t)
    return X, Y


def main(a, b, k, h, x, y, period):
    X_e, Y_e = Euler(a, b, k, h, y, x, period)
    X_a, Y_a = Analytic(a, b, k, x, y, h, period)
    plt.title("Secretion of hormones " + 'MSE = ' + str(mean_squared_error(Y_e, Y_a)))
    plt.plot(X_e, Y_e, c="green", label="euler")
    plt.plot(X_a, Y_a, c="red", label="analytical")
    plt.grid(True)
    plt.xlabel("Time")
    plt.ylabel("Level")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    b = 1
    a = 1
    h = 0.001
    k = 2
    x0 = 0.1
    y0 = 0
    main(a, b, k, h, x0, y0, period=100)
