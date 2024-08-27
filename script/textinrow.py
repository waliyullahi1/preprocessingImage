import cv2
import pytesseract

# Read the image
img = cv2.imread(".ocr/dillated.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding (e.g., OTSU threshold)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract text lines and apply OCR
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    text_line = img[y:y + h, x:x + w]
    text = pytesseract.image_to_string(text_line)
    print("Text in row:", text)

# Display or save the results as needed
