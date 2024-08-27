import cv2

# Load the image
image = cv2.imread(".ocr/dillated.jpg")

# Pre-processing (thresholding)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours and draw bounding rectangles
rectangles = []
for contour in contours:
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    if area > 100 and aspect_ratio > 2:  # Filter criteria
        rectangles.append((x, y, w, h))

# Sort rectangles by y-coordinate
rectangles.sort(key=lambda x: x[1])

# Split rows
rows = []
current_row = []
for rectangle in rectangles:
    if not current_row or rectangle[1] - current_row[-1][1] < 10:  # Row grouping criteria
        current_row.append(rectangle)
    else:
        rows.append(current_row)
        current_row = [rectangle]
rows.append(current_row)

# Draw rectangles around rows
for row in rows:
    if row:  # Check if row is not empty
        x_min = min(rectangle[0] for rectangle in row)
        y_min = min(rectangle[1] for rectangle in row)
        x_max = max(rectangle[0] + rectangle[2] for rectangle in row)
        y_max = max(rectangle[1] + rectangle[3] for rectangle in row)
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

# Display the output
cv2.imshow('Rows', image)
cv2.waitKey(0)
cv2.destroyAllWindows()