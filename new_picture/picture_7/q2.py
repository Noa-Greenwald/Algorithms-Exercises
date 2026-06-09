import sys
#א

import numpy as np

LEARNING_RATE = 0.1
NUM_ITERATIONS = 1000


def z(x, y):
    return np.sin(x) + np.sin(y)


def gradient(x, y):
    dz_dx = np.cos(x)
    dz_dy = np.cos(y)

    return dz_dx, dz_dy


def gradient_descent(x, y):

    for _ in range(NUM_ITERATIONS):

        dz_dx, dz_dy = gradient(x, y)

        x = x - LEARNING_RATE * dz_dx
        y = y - LEARNING_RATE * dz_dy

    return x, y


x0 = float(sys.argv[1])
y0 = float(sys.argv[2])

print(
    f"Starting point: x={x0:.4f}, y={y0:.4f}, z={z(x0,y0):.4f}"
)

xmin, ymin = gradient_descent(x0, y0)

print(
    f"Minimum found: x={xmin:.4f}, y={ymin:.4f}, z={z(xmin,ymin):.4f}"
)

#ב
path_x = []
path_y = []

for _ in range(NUM_ITERATIONS):

    path_x.append(x)
    path_y.append(y)

    dz_dx = np.cos(x)
    dz_dy = np.cos(y)

    x -= LEARNING_RATE * dz_dx
    y -= LEARNING_RATE * dz_dy

    import matplotlib.pyplot as plt

    plt.plot(path_x, path_y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gradient Descent Path")
    plt.grid()
    plt.show()

    changes = []

    for i in range(1, len(path_x)):
        dx = path_x[i] - path_x[i - 1]
        dy = path_y[i] - path_y[i - 1]

        changes.append(np.sqrt(dx ** 2 + dy ** 2))

    plt.plot(changes)
    plt.title("Change Size Per Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Step Size")
    plt.grid()
    plt.show()