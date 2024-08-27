import cv2
from PIL import Image

import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image =  cv2.imread(".ocr/hhhf.jpg")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.AdaptiveThresholdTypes(grayImage, 0, 255, cv2.THRESH_BINARY_INV)
#_, threshold = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY_INV)

# img_no_niose = Image.open(".ocr/no.jpg")
# img = Image.open(".ocr/lessn.jpg")

# ocr_result = pytesseract.image_to_string(img_no_niose)

cv2.imshow("threshold", threshold)
cv2.imshow("grayImage", grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
