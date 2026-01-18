#א
import cv2
import numpy as np
from Exercise2_picture.create_test_images import create_circle_image

img = create_circle_image(400, 500, bg=100, fg=105)
cv2.imwrite('low_contrast_circle.png', img)

#ב
# קריאה לתמונה בגווני אפור
src = cv2.imread('low_contrast_circle.png', cv2.IMREAD_GRAYSCALE)

# חישוב מינימום, מקסימום וממוצע
min_val = np.min(src)
max_val = np.max(src)
mean_val = np.mean(src)

# חישוב הפקטור למתיחת הניגודיות
factor = 255 / (max_val - min_val)

print("Min pixel value:", min_val)
print("Max pixel value:", max_val)
print("Mean pixel value:", mean_val)
print("Max scaling factor (255 / (max-min)):", factor)


#ג
def normalize(img):
    # המרה ל-float32 כדי לא לאבד דיוק
    img_float = img.astype(np.float32)

    # חישוב מינימום ומקסימום
    min_val = np.min(img_float)
    max_val = np.max(img_float)

    # חישוב הפקטור למתיחה
    factor = 255.0 / (max_val - min_val)

    # ביצוע normalization
    dst_float = (img_float - min_val) * factor

    # החזרת התמונה ל-type uint8
    dst = np.clip(dst_float, 0, 255).astype(np.uint8)

    return dst

#ד
normalized_img = normalize(src)

cv2.imwrite('low_contrast_circle_normalized.png', normalized_img)

# נבדוק מינימום ומקסימום אחרי normalization
print("After normalization:")
print("Min:", np.min(normalized_img))
print("Max:", np.max(normalized_img))
