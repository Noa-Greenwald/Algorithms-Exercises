#א
import numpy as np

from new_picture.picture_1.q1 import deg2rad


def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# דוגמה – סיבוב של 45 מעלות
theta = deg2rad(45)
R = rotation_matrix(theta)
print("Rotation matrix (45 degrees):")
print(R)

#ב
scale_all = np.array([
    [2, 0],
    [0, 2]
])

print("Scale x2 (both axes):")
print(scale_all)

#ג
scale_x = np.array([
    [2, 0],
    [0, 1]
])

print("Scale x2 (x-axis only):")
print(scale_x)

