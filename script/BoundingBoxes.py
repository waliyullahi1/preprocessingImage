import cv2
from PIL import Image
import numpy as np
img = cv2.imread(".ocr/BoundingBoxes.jpg")
img = cv2.resize(img, (700, 700))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# inverted = cv2.bitwise_not(img)

blur = cv2.GaussianBlur(gray, (7,7), 0)

# img = cv2.imread(".ocr/lessn.jpg")
threshold = cv2.threshold(blur, 0,255, cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)[1]
# cv2.imshow("img", img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 12))



dilate = cv2.dilate(threshold, kernel, iterations=1)


cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

cnts=sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if h > 200 and w > 20:
        cv2.rectangle(img, (x,y), (x+y, y+h), (16, 255,12), 1)

    
cv2.imshow("dilate", dilate)
cv2.imshow("glur", kernel)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()