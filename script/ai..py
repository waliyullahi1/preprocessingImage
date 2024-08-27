import cv2
import numpy as np

# Load the image
image_path = 'your_image.jpg'  # Change this to your image path
image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print("Error: could not load image.")
    exit()

# Get the height and width of the image
height, width = image.shape[:2]

# Create a blank template image (black) with the same dimensions
# You can change the color (black by default) if needed
template = np.zeros((height, width, 3), dtype=np.uint8)

# Optionally, fill the template with a specific color (e.g., white)
# template[:] = (255, 255, 255)  # This would make it all white

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Template", template)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
