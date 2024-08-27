import cv2
from PIL import Image
import numpy as np
img = cv2.imread(".ocr/lessn.jpg")
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


#remove border or background
def remove_borders(image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    return (crop)

no_borders = remove_borders(img_no_noise_remover)
#Missing Borders
color = [255, 255, 255]
top, bottom, left, right = [150]*4
image_with_border = cv2.copyMakeBorder(no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
cv2.imwrite("temp/image_with_border.jpg", image_with_border)


cv2.imshow("imge", img)
cv2.imshow("no_borders", no_borders)
cv2.waitKey(0)
cv2.destroyAllWindows()