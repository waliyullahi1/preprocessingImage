import numpy as np
import cv2
import pytesseract
img = cv2.imread(".ocr/dillated.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print( str(len(contours))) 
#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    
    if cv2.contourArea(cnt) > 1000:
        crop = img[y:y+h, x:x+w]
        data = pytesseract.image_to_data(crop, output_type=pytesseract.Output.DICT)
        cv2.rectangle(img, (x, y),(x+w, y+h), (0, 0, 255), 1 )
        data = str(data)
        cv2.putText(img, data, (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0), 2 )


# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
   
#     text_line = img[y:y + h, x:x + w]
  
#     cv2.imshow("cnt", img)
#     cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
#     cv2.putText(img, "triangle", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,0) )

cv2.imshow('img', img)
cv2.imshow("IMAGE GRAY", imgray)
# dat=
cv2.waitKey(0)
cv2.destroyAllWindows()