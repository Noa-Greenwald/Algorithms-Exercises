import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

result_x = cross_correlation(image, sobel_x)
result_y = cross_correlation(image, sobel_y)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(image, cmap='gray')
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Sobel X")
plt.imshow(result_x, cmap='gray')
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Sobel Y")
plt.imshow(result_y, cmap='gray')
plt.axis("off")

plt.show()