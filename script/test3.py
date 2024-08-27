import cv2
import numpy as np
from PIL import Image

# Load the image
image = cv2.imread(".ocr/hhhf.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to get a binary image
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Invert the thresholded image
thresh = cv2.bitwise_not(thresh)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask of the same size as the image, filled with zeros (black)
mask = np.zeros_like(image)

# Draw the contours on the mask
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Invert the mask
mask = cv2.bitwise_not(mask)

# Convert the mask to grayscale
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Create a 4-channel image (RGBA) with the original image and the mask
result = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask_gray

# Save the result
# cv2.imwrite('output.png', result)

# Display the result
cv2.imshow('Result', result)
cv2.imshow('Result', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
