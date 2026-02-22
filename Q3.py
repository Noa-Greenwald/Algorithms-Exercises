import sys
import cv2
import numpy as np

# --------------------------
# בדיקת קלט
# --------------------------
if len(sys.argv) != 4:
    print("Usage: python rgb_convert.py R G B")
    sys.exit(1)

R, G, B = map(int, sys.argv[1:4])

r = R / 255.0
g = G / 255.0
b = B / 255.0

Cmax = max(r, g, b)
Cmin = min(r, g, b)
delta = Cmax - Cmin

# --------------------------
# HSV - חישוב ידני
# --------------------------
if delta == 0:
    H = 0
elif Cmax == r:
    H = 60 * (((g - b) / delta) % 6)
elif Cmax == g:
    H = 60 * (((b - r) / delta) + 2)
else:
    H = 60 * (((r - g) / delta) + 4)

S = 0 if Cmax == 0 else delta / Cmax
V = Cmax

HSV_manual = (H, S, V)

# --------------------------
# HSL - חישוב ידני
# --------------------------
L = (Cmax + Cmin) / 2

if delta == 0:
    S_l = 0
else:
    S_l = delta / (1 - abs(2*L - 1))

HSL_manual = (H, S_l, L)

# --------------------------
# YCrCb - חישוב ידני
# --------------------------
Y  = 0.299*R + 0.587*G + 0.114*B
Cr = (R - Y) * 0.713 + 128
Cb = (B - Y) * 0.564 + 128

YCrCb_manual = (Y, Cr, Cb)

# --------------------------
# OpenCV חישוב
# --------------------------
rgb = np.uint8([[[B, G, R]]])  # OpenCV עובד ב-BGR

HSV_cv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)[0][0]
HSL_cv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HLS)[0][0]
YCrCb_cv = cv2.cvtColor(rgb, cv2.COLOR_BGR2YCrCb)[0][0]

# --------------------------
# הדפסה
# --------------------------
print("\n--- Manual ---")
print("HSV:", HSV_manual)
print("HSL:", HSL_manual)
print("YCrCb:", YCrCb_manual)

print("\n--- OpenCV ---")
print("HSV:", HSV_cv)
print("HSL:", HSL_cv)
print("YCrCb:", YCrCb_cv)
