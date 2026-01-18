import matplotlib.pyplot as plt

from q1 import create_gradient_image
from q2 import brighten


if __name__ == "__main__":
    height = 400
    width = 500
    b = 80

    # יצירת התמונה משאלה 1
    img = create_gradient_image(height, width)

    # הבהרה בעזרת np.add
    bright_np = brighten(img, b, "np")

    # הבהרה בעזרת cv2.add
    bright_cv2 = brighten(img, b, "cv2")

    # הצגה עם matplotlib
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    axes[0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[0].set_title("Original")
    axes[0].axis('off')

    axes[1].imshow(bright_np, cmap='gray', vmin=0, vmax=255)
    axes[1].set_title("brighten with np.add")
    axes[1].axis('off')

    axes[2].imshow(bright_cv2, cmap='gray', vmin=0, vmax=255)
    axes[2].set_title("brighten with cv2.add")
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()
