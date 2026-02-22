#א
import numpy as np
def deg2rad(deg):
    return deg * np.pi / 180
print(deg2rad(180))
print(deg2rad(90))

#ב
angles = [0, 90, 180, 45, 30, 10, 5, 1]
results = []

for deg in angles:
    rad = deg2rad(deg)
    s = np.sin(rad)
    c = np.cos(rad)

    results.append([deg, rad, s, c])

#ג
results_array = np.array(results)

np.savetxt(
    "trig_results.csv",
    results_array,
    delimiter=",",
    header="degrees,radians,sin,cos",
    comments=""
)