import numpy as np

# פונקציה להמרת מעלות לרדיאנים
def degrees_to_radians(degrees):
    return degrees * np.pi / 180


degrees_list = [0, 90, 180, 45, 30, 10, 5, 1]

print("degrees,radians,sin,cos")

for deg in degrees_list:
    rad = degrees_to_radians(deg)
    sin_val = np.sin(rad)
    cos_val = np.cos(rad)

    print(f"{deg},{rad:.6f},{sin_val:.6f},{cos_val:.6f}")