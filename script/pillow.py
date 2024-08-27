import cv2
from PIL import Image
import pytesseract
#https://talkai.info/chat/
img = Image.open(".ocr/note.jpg")
print(img.size)
img.rotate(90).show() 

cr_result = pytesseract.image_to_string(img)
print(cr_result)
