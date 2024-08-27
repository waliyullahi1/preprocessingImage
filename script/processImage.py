#Open CV
import cv2
from PIL import Image
import numpy as np
img = cv2.imread(".ocr/aa.jpg")
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# print(img.size)
# img.rotate(90).show() 
# img = cv2.resize(img, (512, 512))

#inverted Images
inverted = cv2.bitwise_not(img)


# Rescaling


#Binarization
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )


grayImage= grayscale(img) 

_, threshold  = cv2.threshold(grayImage, 200, 255, cv2.THRESH_BINARY)




#Noise remove  

def noise_remover(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
   
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
  
    image= cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
 
    image = cv2.medianBlur(image, 3)
  
    return (image)



def noise_remover2(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
 
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
  
    image= cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("morphologyEx", image)
   
    return (image)

img_no_noise_remover = noise_remover(threshold)







#Dillation and Erosin
def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)



erroded_image = thin_font(img_no_noise_remover)

dilated_image = thick_font(img_no_noise_remover)

ocr_result = pytesseract.image_to_string(dilated_image)

cv2.imwrite(".ocr/aaa.jpg", dilated_image)
print(ocr_result)

# cv2.imshow("grayImage", threshold)
# cv2.imshow("img_no_noise_remover", img_no_noise_remover)
cv2.imshow("erroded_image", erroded_image)
cv2.imshow("dilated_image", dilated_image)
cv2.imshow("imge", img)
# cv2.imshow("inverted", inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()