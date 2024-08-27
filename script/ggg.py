import cv2
import pytesseract

# Read the image
img = cv2.imread(".ocr/dillated.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contours, heiarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print( str(len(contours))) 
cv2.drawContours(img, contours, 0, (0, 255, 0), 1)
# def remove_borders(image):
#     contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
#     cnt = cntsSorted[-1]
#     x, y, w, h = cv2.boundingRect(cnt)
#     crop = image[y:y+h, x:x+w]
#     return (crop)
# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding (e.g., OTSU threshold)
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Find contours
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# ocr_result = pytesseract.image_to_string(img_no_niose)
# Extract text lines and apply OCR
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     text_line = img[y:y + h, x:x + w]
#     cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
#     text = remove_borders(cnt)
#     ocr_result = pytesseract.image_to_string(text)

    #cv2.imshow("cnt", img)
   
# def remove_borders(image):
#     contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
#     cnt = cntsSorted[-1]
#     x, y, w, h = cv2.boundingRect(cnt)
#     crop = image[y:y+h, x:x+w]
#     cv2.imshow("image",crop)
#     return (crop)
# Convert to grayscale
# remove_borders(img)
   

cv2.imshow("image",img)
# Display or save the results as neede
cv2.waitKey(0)
cv2.destroyAllWindows()