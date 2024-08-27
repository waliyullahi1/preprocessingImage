import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('.ocr/hhhf.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# Calculate the average intensity
average_intensity = np.mean(gray)

# Determine if the image is dark
threshold = 50  # You can adjust this threshold value
if average_intensity < threshold:
    print("The image is dark or taken at night.")
else:
    print("The image is not dark.")

print(f"Average Intensity: {average_intensity}")
