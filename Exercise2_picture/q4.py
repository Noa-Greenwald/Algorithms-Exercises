import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_low_contrast_image(fg, bg, height=400, width=400):
    # יצירת תמונה מלאה בצבע הרקע
    img = np.full((height, width), fill_value=bg, dtype=np.uint8)

    # פרמטרים של העיגול
    center = (width // 2, height // 2)
    radius = min(height, width) // 4

    # ציור עיגול בצבע החזית
    cv2.circle(
        img,
        center=center,
        radius=radius,
        color=fg,
        thickness=-1   # עיגול מלא
    )

    return img


if __name__ == "__main__":
    # ערכים קרובים -> ניגודיות נמוכה
    fg = 105   # צבע החזית
    bg = 100   # צבע הרקע

    img = create_low_contrast_image(fg, bg)

    # הצגה עם matplotlib
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title("Low Contrast Image")
    plt.axis('off')
    plt.show()
