import numpy as np
import cv2


def brighten(img, b, func):

    if func == "np":
        return np.add(img, b)

    elif func == "cv2":
        return cv2.add(img, b)

    else:
        raise ValueError("func must be 'np' or 'cv2'")


if __name__ == "__main__":
    # דוגמה קצרה לבדיקה
    img = np.array([[250, 251],
                    [252, 253]], dtype=np.uint8)

    b = 10

    bright_np = brighten(img, b, "np")
    bright_cv2 = brighten(img, b, "cv2")

    print("Original image:\n", img)
    print("Using np.add:\n", bright_np)
    print("Using cv2.add:\n", bright_cv2)
