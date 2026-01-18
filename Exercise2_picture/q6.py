import numpy as np
import cv2
import matplotlib.pyplot as plt

def normalize(img):
    img_float = img.astype(np.float32)
    min_val = np.min(img_float)
    max_val = np.max(img_float)
    factor = 255.0 / (max_val - min_val)
    dst_float = (img_float - min_val) * factor
    dst = np.clip(dst_float, 0, 255).astype(np.uint8)
    return dst

# קריאת התמונה המקורית
img = cv2.imread("low_contrast_circle.png", cv2.IMREAD_GRAYSCALE)

# שינוי פיקסלים קיצוניים
img_modified = img.copy()
img_modified[0, 0] = 0
img_modified[100, 100] = 255

# normalization
normalized_img_modified = normalize(img_modified)

# הצגה
plt.subplot(1,2,1)
plt.imshow(img_modified, cmap='gray', vmin=0, vmax=255)
plt.title("Modified Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(normalized_img_modified, cmap='gray', vmin=0, vmax=255)
plt.title("Normalized Modified Image")
plt.axis('off')

plt.show()

# בדיקת סטטיסטיקות
print("Modified Image - Min:", np.min(img_modified), "Max:", np.max(img_modified))
print("Normalized Modified Image - Min:", np.min(normalized_img_modified), "Max:", np.max(normalized_img_modified))
