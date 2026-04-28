import numpy as np


# א
def rotation_matrix(theta):
    theta_rad = np.deg2rad(theta)

    return np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)],
        [np.sin(theta_rad),  np.cos(theta_rad)]
    ])


# ב
def scale_uniform_2():
    return np.array([
        [2, 0],
        [0, 2]
    ])


# ג
def scale_x_2():
    return np.array([
        [2, 0],
        [0, 1]
    ])