import cv2
import pytesseract
from docx import Document
from PIL import Image
#9519010580
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#https://talkai.info/chat/
print('begining')

image =  cv2.imread(".ocr/aa.jpg")

def img_to_word(img_path, output_docx):
    # Read the image
    img = cv2.imread(img_path)

    # Convert to RGB (pytesseract requires RGB images)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Perform OCR on the image
    data = pytesseract.image_to_data(img_rgb, output_type=pytesseract.Output.DICT)

    # Create a new Document
    doc = Document()
    
    # Loop through each word detected
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:  # Confidence threshold
            text = data['text'][i]
            x = data['left'][i]
            y = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]

            # Add text to the document at a specific position
            # For now, we simply add the text to the next line
            doc.add_paragraph(text)
            print("done")
            # Optional: You can use x, y, width, height to improve the layout later

    # Save the Document
    doc.save(output_docx)

    print(f"Document saved as {output_docx}")

img_to_word('.ocr/dillated.jpg', 'output1.docx')