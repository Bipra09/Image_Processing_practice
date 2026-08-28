import cv2
import numpy as np

img = cv2.imread(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg", cv2.IMREAD_GRAYSCALE)

# 1. Mean filter
mean = cv2.blur(img, (3, 3))
cv2.imwrite("1_mean.png", mean)

# 2. Gaussian filter
gaussian = cv2.GaussianBlur(img, (3, 3), sigmaX=1)
cv2.imwrite("2_gaussian.png", gaussian)

# 3. Median filter
median = cv2.medianBlur(img, 3)
cv2.imwrite("3_median.png", median)

# 4. Otsu's thresholding
_, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite("4_otsu.png", otsu)

# 5. Dilation / Erosion (needs binary image first — reuse otsu output)
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(otsu, kernel, iterations=1)
eroded = cv2.erode(otsu, kernel, iterations=1)
cv2.imwrite("5_dilate.png", dilated)
cv2.imwrite("5_erode.png", eroded)

# 6. Sobel filter
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobel_x**2 + sobel_y**2)
sobel = np.uint8(np.clip(sobel, 0, 255))
cv2.imwrite("6_sobel.png", sobel)

# 7. Canny edge detector
canny = cv2.Canny(img, 100, 200)
cv2.imwrite("7_canny.png", canny)

print("done")