import cv2

# Load image in grayscale
img = cv2.imread('.ocr/hhhf.jpg', 0)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY_INV, 11, 2)

# Apply morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilated = cv2.dilate(thresh, kernel, iterations=2)
eroded = cv2.erode(dilated, kernel, iterations=1)

# Find and draw contours
contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key=cv2.contourArea)

# Draw the largest contour on the original image
cv2.drawContours(img, [largest_contour], -1, (0, 255, 0), 2)

# for cnt in contours:
#     if cv2.contourArea(cnt) > 1000:  # Adjust the area threshold as needed
#         cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('errr', eroded)
cv2.imshow('imag', kernel)
cv2.imshow('imsag', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
