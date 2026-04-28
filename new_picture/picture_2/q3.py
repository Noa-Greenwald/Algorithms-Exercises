import numpy as np
import matplotlib.pyplot as plt


# =========================
# מטריצת סיבוב 30 מעלות
# =========================
theta = np.deg2rad(30)

r_30 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

print("r_30 =")
print(r_30)


# =========================
# מטריצת scale פי 2 בציר x
# =========================
sx_2 = np.array([
    [2, 0],
    [0, 1]
])

print("\nsx_2 =")
print(sx_2)


# =========================
# חישוב rs ו-sr
# =========================
rs = r_30 @ sx_2
sr = sx_2 @ r_30

print("\nrs = r_30 @ sx_2")
print(rs)

print("\nsr = sx_2 @ r_30")
print(sr)


# =========================
# יצירת מלבן: רוחב 2, גובה 1, מרכז בראשית
# =========================
rectangle = np.array([
    [-1, -0.5],
    [ 1, -0.5],
    [ 1,  0.5],
    [-1,  0.5],
    [-1, -0.5]   # סוגרים את הצורה
])


# =========================
# הפעלת הטרנספורמציות
# =========================
rect_rot = (r_30 @ rectangle.T).T
rect_scale = (sx_2 @ rectangle.T).T
rect_rs = (rs @ rectangle.T).T
rect_sr = (sr @ rectangle.T).T


# =========================
# ציור כל המלבנים
# =========================
plt.figure(figsize=(8,8))

plt.plot(rectangle[:,0], rectangle[:,1], label="Original")
plt.plot(rect_rot[:,0], rect_rot[:,1], label="Rotate 30°")
plt.plot(rect_scale[:,0], rect_scale[:,1], label="Scale x2")
plt.plot(rect_rs[:,0], rect_rs[:,1], label="r_30 @ sx_2")
plt.plot(rect_sr[:,0], rect_sr[:,1], label="sx_2 @ r_30")

plt.axhline(0)
plt.axvline(0)

plt.gca().set_aspect('equal', 'box')
plt.legend()
plt.title("Rectangle Transformations")
plt.show()